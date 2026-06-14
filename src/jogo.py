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
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
    verificar_posicao,
    exibe_mensagem
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
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

    # 1. Carregando as imagens recortadas do Spritesheet


    # frangonauta: usando tamanho 980x1080 para capturar o quadrado perfeitamente
    frangonauta_image = pegar_sprite("assets/imagens/frangonauta.png", x=0, y=0, width=980, height=1080, scale=0.2)
    
    # batata pequena: usando tamanho 900x1400
    batata_image    = pegar_sprite("assets/imagens/batata.png", x=0, y=0, width=1400, height=900, scale=0.2)

    # Morcego: usando tamanho 900x1200 por causa das asas abertas
    meteoro_image = pegar_sprite("assets/imagens/Meteor1.png", x=0, y=0, width=1200, height=900, scale=0.15)
    # 2. Criando a estrutura de Sprites usando Dicionários
    x_frangonauta = 150
    y_frangonauta = 150

    frangonauta = {
        "imagem": frangonauta_image,
        "rect": frangonauta_image.get_rect(topleft=(100, 300)).inflate(-50, -50)
    }

    batata = {
        "imagem": batata_image,
        "rect": batata_image.get_rect(topleft=(500, 300)).inflate(-110, -110)
    }
    
    meteoro = {
        "imagem": meteoro_image,
        "rect": meteoro_image.get_rect(topleft=(LARGURA_TELA, 300)).inflate(-50, -100) # reduz o hitbox
    }

    gravidade = 2
    velocidade = 150
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)
    tempo_inicial = pygame.time.get_ticks()
    TEMPO_VITORIA = 90 # tempo para ganhar o jogo

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
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

        # Movimentação alterando direto o eixo Y do retângulo do frangonauta
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    frangonauta["rect"].y -= velocidade
            
        # Gravidade   
        frangonauta["rect"].y += gravidade
        meteoro["rect"].x -= 8  # velocidade do meteoro
        batata["rect"].x -= 6

        # Limitando o frangonauta dentro das bordas da tela usando as propriedades do Rect
        frangonauta["rect"].x = limitar_valor(frangonauta["rect"].x, 0, LARGURA_TELA - frangonauta["rect"].width)
        frangonauta["rect"].y = limitar_valor(frangonauta["rect"].y, 0, ALTURA_TELA - frangonauta["rect"].height)

        # Verificação de colisão com a batata
        if verificar_colisao(frangonauta["rect"], batata["rect"]):
            pontos = calcular_pontos(pontos, 10)

            # Move a batata de lugar ao coletar
            batata["rect"].x = -1000 # joga a batata para longe
            batata["rect"].y = -1000

            # Se a batata sair da tela, volta para uma posição segura
            if batata["rect"].x > LARGURA_TELA - batata["rect"].width:
                batata["rect"].x = 50
            if batata["rect"].y > ALTURA_TELA - batata["rect"].height:
                batata["rect"].y = 50

        # Verificação de colisão com o meteoro
        if verificar_colisao(frangonauta["rect"], meteoro["rect"]):
            vidas = tomar_dano(vidas, 1)
            meteoro["rect"].x = -1000 # joga o meteoro para longe prevenindo dano inesperado
            meteoro["rect"].y = -1000

        if verificar_posicao(meteoro, LARGURA_TELA):
            # Novo meteoro a cada momento
            numero_aleatorio_y = random.randint(1, ALTURA_TELA)
            meteoro["rect"].x = LARGURA_TELA
            meteoro["rect"].y = numero_aleatorio_y
            # Nova batata a cada momento
            numero_aleatorio_y = random.randint(10, ALTURA_TELA)
            batata["rect"].x = LARGURA_TELA
            batata["rect"].y = numero_aleatorio_y
        
        # Regras de fim de jogo e recorde
        if jogador_perdeu(vidas):
            game_over = exibe_mensagem("PERDEU O JOGO!", 40, ( 100 , 0 , 0 ) )
            tela.blit( game_over , (LARGURA_TELA // 2 , ALTURA_TELA // 2 ) )
            pygame.display.flip()
            pygame.time.wait(4000)  # espera 4 segundos para aparecer a mensagem
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Tempo: {tempo_decorrido}s | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        tela.fill(PRETO)

        # Desenhando os elementos na tela passando a imagem e o rect de cada dicionário
        tela.blit(batata["imagem"], batata["rect"])
        tela.blit(meteoro["imagem"], meteoro["rect"])
        tela.blit(frangonauta["imagem"], frangonauta["rect"])


        pygame.display.flip()

    pygame.quit()