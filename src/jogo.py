import pygame
import random

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    PRETO,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
    CAMINHO_RANKING
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    criar_objeto,
    movimentacao_jogador,
    movimentacao_objeto,
    exibe_mensagem,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    salvar_ranking
)

from src.menu import menu

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    if not menu():
        pygame.quit()
        return

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True
    
    """ class do meteoro"""
    meteoro_x = LARGURA_TELA
    meteoro_y = 0
    meteoro__largura = 214
    meteoro__altura = 61
    class Meteoro(pygame.Rect):
        def __init__(self, img):
            pygame.Rect.__init__(self, meteoro_x, meteoro_y, meteoro__largura, meteoro__altura)
            self.img = img    
    
    """class do batata"""
    batata_x = LARGURA_TELA
    batata_y = 0
    batata__largura = 100/1.5
    batata__altura = 61/1.5
    class Batata(pygame.Rect):
        def __init__(self, img):
            pygame.Rect.__init__(self, batata_x, batata_y, batata__largura, batata__altura)
            self.img = img        

    """class do frangonauta"""
    x_jogador = 125
    y_jogador = 150
    largura_jogador = 212/1.5
    altura_jogador = 124
    class Frango(pygame.Rect):
        def __init__(self, img):
            pygame.Rect.__init__(self, x_jogador, y_jogador, largura_jogador, altura_jogador)
            self.img = img
            self.passed = False

    """lista de meteoros e batatas que serão criados"""
    meteoros = []

    """lista de batatas que serão criados"""
    batatas = []

    """imagens dos objetos"""
    frango_imagem = pygame.image.load("assets/imagens/frangonauta.png")
    frango_imagem = pygame.transform.scale(frango_imagem, (largura_jogador, altura_jogador))
    meteoro_imagem = pygame.image.load("assets/imagens/Meteor1.png")
    meteoro_imagem = pygame.transform.scale(meteoro_imagem, (meteoro__largura, meteoro__altura))
    batata_imagem = pygame.image.load("assets/imagens/batata.png")
    batata_imagem = pygame.transform.scale(batata_imagem, (batata__largura, batata__altura))
    
    """atribuição das variáveis"""
    frango = (Frango(frango_imagem))
    meteoro = (Meteoro(meteoro_imagem))
    batata = (Batata(batata_imagem))

    """básicos"""
    velocidade_meteoro = -10
    velocidade_Batata = -5
    velocidade_frango = 0
    gravidade = 0.35
    pontos = 0
    pontuacoes = []
    pontos_anteriores = pontos
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)
    tempo_inicial = pygame.time.get_ticks()
    TEMPO_VITORIA = 35 # tempo para ganhar o jogo

    """timer para quando os meteoros são criados"""
    criar_meteoro_tempo = pygame.USEREVENT + 0
    pygame.time.set_timer(criar_meteoro_tempo, 1000) #1 segundos

    """timer para quando as batatas são criadas"""
    criar_batata_tempo = pygame.USEREVENT + 2
    pygame.time.set_timer(criar_batata_tempo, 2000) #2 segundos

    """analisar se já perdeu dano ou recebeu a pontuação do objeto"""
    colisão_pontos = False
    colisão_vida = False

    """timer do estágio"""
    timer = pygame.time.get_ticks()

    """loop principal: processa entrada, atualiza estado e renderiza a cena."""
    while rodando:

        tempo_decorrido = (pygame.time.get_ticks() - tempo_inicial) // 1000
        if tempo_decorrido >= TEMPO_VITORIA:
            game_win = exibe_mensagem("VOCÊ VENCEU!", 40 , ( 0 , 100 , 0) )
            tela.blit( game_win , (LARGURA_TELA // 2 , ALTURA_TELA // 2 ) )
            pygame.display.flip()
            pygame.time.wait(4000)  # espera 4 segundos para aparecer a mensagem
            rodando = False
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == criar_meteoro_tempo:
                criar_objeto(meteoros, meteoro_imagem, Meteoro, ALTURA_TELA)

            if evento.type == criar_batata_tempo:
                criar_objeto(batatas, batata_imagem, Batata, ALTURA_TELA)

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    velocidade_frango = -10
            
        """função de movimentação dos elementos e gravidade"""
        movimentacao_jogador(velocidade_frango, frango)
        velocidade_frango += gravidade
        movimentacao_objeto(batatas, velocidade_Batata)
        movimentacao_objeto(meteoros, velocidade_meteoro)

        """limite de tela"""
        frango.y = max(frango.y, -10)
        frango.y = min(frango.y, ALTURA_TELA-100)

        """mensagens de fim de jogo e recorde"""
        if jogador_perdeu(vidas):
            game_over = exibe_mensagem("PERDEU O JOGO!", 40, ( 100 , 0 , 0 ) )
            tela.blit( game_over , (LARGURA_TELA // 2 , ALTURA_TELA // 2 ) )
            pygame.display.flip()
            pygame.time.wait(4000)  # espera 4 segundos para aparecer a mensagem
            rodando = False

        """pontuação das batatas"""
        if verificar_colisao(frango, batata):
            if colisão_pontos == False:
                colisão_pontos = True
                pontos = calcular_pontos(pontos, 15)
                batata.y = -50
        else:
            colisão_pontos = False

        """vida restante"""
        if verificar_colisao(frango, meteoro):
            if colisão_vida == False:
                colisão_vida = True
                vidas = tomar_dano(vidas, 1)
        else:
            colisão_vida = False

        """listando as pontuações da partida atual"""
        if pontos > pontos_anteriores:
            pontuacoes.append(pontos)
        pontos_anteriores

        """obtenção de record"""
        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        """obtenção do ranking"""
        if pontos != pontos_anteriores:
            salvar_ranking(CAMINHO_RANKING, pontos)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Tempo: {tempo_decorrido}s | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        tela.fill(PRETO)

        for meteoro in meteoros:
            tela.blit(meteoro.img, meteoro)
        tela.blit(frango.img, frango)
        for batata in batatas:
            tela.blit(batata.img, batata)

        pygame.display.flip()

    pygame.quit()