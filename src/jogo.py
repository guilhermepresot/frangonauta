import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    PRETO,
    CAMINHO_RECORDE,
    VERMELHO,
    VERDE,
    BRANCO
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    verificar_colisao,
    tomar_dano,
    criar_objeto,
    movimentacao_jogador,
    movimentacao_objeto,
    exibe_mensagem,
)
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)

from src.menu import menu
from src.fim import (
    salvo
)

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    recorde_arq = carregar_recorde(CAMINHO_RECORDE)

    pygame.init()
    if not menu(recorde_arq):
        pygame.quit()
        return

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True
    
    """Class do meteoro"""
    meteoro_x = LARGURA_TELA
    meteoro_y = 0
    meteoro__largura = 214
    meteoro__altura = 61
    class Meteoro(pygame.Rect):
        def __init__(self, img):
            pygame.Rect.__init__(self, meteoro_x, meteoro_y, meteoro__largura, meteoro__altura)
            self.img = img    
    
    """Class do batata"""
    batata_x = LARGURA_TELA
    batata_y = 0
    batata__largura = 100/1.5
    batata__altura = 40
    class Batata(pygame.Rect):
        def __init__(self, img):
            pygame.Rect.__init__(self, batata_x, batata_y, batata__largura, batata__altura)
            self.img = img        

    """Class do frangonauta"""
    x_jogador = 125
    y_jogador = 150
    largura_jogador = 212/1.5
    altura_jogador = 124
    class Frango(pygame.Rect):
        def __init__(self, img):
            pygame.Rect.__init__(self, x_jogador, y_jogador, largura_jogador, altura_jogador)
            self.img = img
            self.passed = False

    """Lista de meteoros e batatas que serão criados"""
    meteoros = []

    """Lista de batatas que serão criados"""
    batatas = []

    """Imagens dos objetos"""
    frango_imagem = pygame.image.load("assets/imagens/frangonauta.png")
    frango_imagem = pygame.transform.scale(frango_imagem, (largura_jogador, altura_jogador))
    meteoro_imagem = pygame.image.load("assets/imagens/Meteor1.png")
    meteoro_imagem = pygame.transform.scale(meteoro_imagem, (meteoro__largura, meteoro__altura))
    batata_imagem = pygame.image.load("assets/imagens/batata.png")
    batata_imagem = pygame.transform.scale(batata_imagem, (batata__largura, batata__altura))
    
    """Atribuição das variáveis"""
    frango = (Frango(frango_imagem))
    meteoro = (Meteoro(meteoro_imagem))
    batata = (Batata(batata_imagem))

    """Básicos"""
    velocidade_meteoro = -10
    velocidade_Batata = -6
    velocidade_frango = 0
    gravidade = 0.35
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)
    tempo_inicial = pygame.time.get_ticks()
    TEMPO_VITORIA = 5 # tempo para ganhar o jogo
    fonte_pontuacoes = pygame.font.SysFont(None, 25)
    ganhou = False

    """Timer para quando os meteoros são criados"""
    criar_meteoro_tempo = pygame.USEREVENT + 0
    pygame.time.set_timer(criar_meteoro_tempo, 1000) #1 segundos

    """Timer para quando as batatas são criadas"""
    criar_batata_tempo = pygame.USEREVENT + 2
    pygame.time.set_timer(criar_batata_tempo, 2000) #2 segundos

    """Analisar se já perdeu dano ou recebeu a pontuação do objeto"""
    colisão_pontos = False
    colisão_vida = False
    colisão_chão = False

    """Loop principal: processa entrada, atualiza estado e renderiza a cena."""
    while rodando:

        relogio.tick(FPS)
        tempo_decorrido = (pygame.time.get_ticks() - tempo_inicial) // 1000
        tempo_restante = TEMPO_VITORIA - tempo_decorrido
        
        """Mensagens de fim de jogo e volta para o Menu Principal"""
        if jogador_perdeu(vidas):
            game_over = exibe_mensagem("Game Over", 50, VERMELHO )
            tela.blit( game_over , ((LARGURA_TELA // 2 - game_over.get_width()//2), (ALTURA_TELA // 2 - game_over.get_height())) )
            pygame.display.flip()
            pygame.time.wait(4000)  # espera 4 segundos para a tela fechar
            executar_jogo()

        """Mensagem de vitória"""
        if tempo_decorrido >= TEMPO_VITORIA:
            ganhou = True
            game_over = exibe_mensagem("Parabéns", 50, VERDE )
            tela.blit( game_over , ((LARGURA_TELA // 2 - game_over.get_width()//2), (ALTURA_TELA // 2 - game_over.get_height())) )
            pygame.display.flip()
            pygame.time.wait(2000)  # espera 2 segundos para a tela fechar
            rodando = False

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            """Cria os objetos que ficam em movimento contínuo (batatas e meteoros)"""
            if evento.type == criar_meteoro_tempo:
                criar_objeto(meteoros, meteoro_imagem, Meteoro, (ALTURA_TELA - meteoro__altura))

            if evento.type == criar_batata_tempo:
                criar_objeto(batatas, batata_imagem, Batata, (ALTURA_TELA - batata__altura))

            """Tecla de movimentação do jogador"""
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    velocidade_frango = -10
            
        """Função de movimentação dos elementos e gravidade"""
        movimentacao_jogador(velocidade_frango, frango)
        velocidade_frango += gravidade
        movimentacao_objeto(batatas, velocidade_Batata)
        movimentacao_objeto(meteoros, velocidade_meteoro)

        """Limite de tela"""
        frango.y = max(frango.y, -10)
        frango.y = min(frango.y, ALTURA_TELA-100)

        if frango.y == ALTURA_TELA-100 and colisão_chão == False:
            vidas = tomar_dano(vidas, 1)
            colisão_chão = True
        if frango.y != ALTURA_TELA-100:
            colisão_chão = False

        """Pontuação das batatas"""
        if verificar_colisao(frango, batata):
            if colisão_pontos == False:
                colisão_pontos = True
                pontos = calcular_pontos(pontos, 15)
                batata.y = -50
        else:
            colisão_pontos = False

        """Vida restante"""
        if verificar_colisao(frango, meteoro):
            if colisão_vida == False:
                colisão_vida = True
                vidas = tomar_dano(vidas, 1)
        else:
            colisão_vida = False

        """oOtenção de record"""
        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO}"
        )

        tela.fill(PRETO)
        
        "Renderiza os objetos"
        for meteoro in meteoros:
            tela.blit(meteoro.img, meteoro)
        tela.blit(frango.img, frango)
        for batata in batatas:
            tela.blit(batata.img, batata)

        "Renderiza na tela todas as pontuacoes (tempo, vida, pontos)"
        texto_pontos = fonte_pontuacoes.render(f"Pontos: {pontos}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))
        texto_vida = fonte_pontuacoes.render(f"Vidas: {vidas}", True, BRANCO)
        tela.blit(texto_vida, (10, 35))
        texto_tempo = fonte_pontuacoes.render(f"Tempo restante: {tempo_restante}", True, BRANCO)
        tela.blit(texto_tempo, ((LARGURA_TELA - texto_tempo.get_width() - 10), 10))

        pygame.display.flip()

    pontuacao = pontos

    if ganhou:
        salvo(pontuacao)

    pygame.quit()