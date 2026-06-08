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
    verificar_posicao
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


    # Jogador: usando tamanho 110x110 para capturar o quadrado perfeitamente
    player_image = pegar_sprite("assets/imagens/frangonauta.png", x=0, y=0, width=980, height=1080, scale=0.2)
    
    # Gema pequena: usando tamanho 64x64
    gem_image    = pegar_sprite("assets/imagens/batata.png", x=0, y=0, width=1400, height=900, scale=0.2)

    # Morcego: usando tamanho 180x120 por causa das asas abertas
    bat_image = pegar_sprite("assets/imagens/Meteor1.png", x=0, y=0, width=1200, height=900, scale=0.15)
    # 2. Criando a estrutura de Sprites usando Dicionários
    x_jogador = 150
    y_jogador = 150
    jogador = {
        "imagem": player_image,
        "rect": player_image.get_rect(topleft=(x_jogador, y_jogador))
    }

    gema = {
        "imagem": gem_image,
        "rect": gem_image.get_rect(topleft=(500, 300))
    }
    
    inimigo = {
        "imagem": bat_image,
        "rect": bat_image.get_rect(topleft=(LARGURA_TELA ,300))
    }

    gravidade = 1
    velocidade = 150
    pontos = 0
    vidas = 300
    recorde = carregar_recorde(CAMINHO_RECORDE)


    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Movimentação alterando direto o eixo Y do retângulo do jogador
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    jogador["rect"].y -= velocidade
            
        # Gravidade   
        jogador["rect"].y += gravidade
        inimigo["rect"].x -= 3

        # Limitando o jogador dentro das bordas da tela usando as propriedades do Rect
        jogador["rect"].x = limitar_valor(jogador["rect"].x, 0, LARGURA_TELA - jogador["rect"].width)
        jogador["rect"].y = limitar_valor(jogador["rect"].y, 0, ALTURA_TELA - jogador["rect"].height)

        # Verificação de colisão com a Gema (antigo 'item')
        if verificar_colisao(jogador["rect"], gema["rect"]):
            pontos = calcular_pontos(pontos, 10)

            # Move a gema de lugar ao coletar
            gema["rect"].x += 80
            gema["rect"].y += 50

            # Se a gema sair da tela, volta para uma posição segura
            if gema["rect"].x > LARGURA_TELA - gema["rect"].width:
                gema["rect"].x = 50
            if gema["rect"].y > ALTURA_TELA - gema["rect"].height:
                gema["rect"].y = 50

        # Verificação de colisão com o Inimigo
        if verificar_colisao(jogador["rect"], inimigo["rect"]):
            vidas = tomar_dano(vidas, 1)

        if verificar_posicao(inimigo, LARGURA_TELA):
            # Novo obstáculo
            numero_aleatorio_y = random.randint(1, ALTURA_TELA)
            inimigo["rect"].x = LARGURA_TELA
            inimigo["rect"].y = numero_aleatorio_y
        
        # Regras de fim de jogo e recorde
        if jogador_perdeu(vidas):
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        tela.fill(PRETO)

        # Desenhando os elementos na tela passando a imagem e o rect de cada dicionário
        tela.blit(gema["imagem"], gema["rect"])
        tela.blit(inimigo["imagem"], inimigo["rect"])
        tela.blit(jogador["imagem"], jogador["rect"])

        pygame.display.flip()

    pygame.quit()