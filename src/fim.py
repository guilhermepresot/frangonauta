import pygame
from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    CAMINHO_RANKING,
    AZUL,
    BRANCO,
    VERMELHO
)
from src.dados import (
    salvar_ranking,
    ler_ranking,
    reordenar_ranking
)

def ranking():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Perdeu")
    fonte = pygame.font.SysFont("Arial", 48)
    fonte_pequena = pygame.font.SysFont("Arial", 32)
    lista_rank = ler_ranking(CAMINHO_RANKING)
    lista = True
    posicao_ranking = 1
    
    rodando = True
    while rodando: 

        titulo_ranking = fonte.render(f"Ranking", True, BRANCO)
        tela.blit(titulo_ranking, (LARGURA_TELA//2 - titulo_ranking.get_width()//2, 75))

        nome = pygame.Rect(100, 175, 200, 60)
        pontuacao = pygame.Rect(500, 175, 200, 60)

        if len(lista_rank) <= 5:
            for valor in range(len(lista_rank)):
                if lista:
                    if valor%2 == 0:
                        texto_nome = fonte_pequena.render(f"Nome: {lista_rank[valor]}", True, BRANCO)
                        tela.blit(texto_nome, (nome.x, nome.y))
                        nome.y += 75
                    else:
                        texto_pontuacao = fonte_pequena.render(f"Pontuacao: {lista_rank[valor]}", True, BRANCO)
                        tela.blit(texto_pontuacao, (pontuacao.x, pontuacao.y))
                        pontuacao.y += 75
        else:
            for valor in range(10):
                if lista:
                    if valor%2 == 0:
                        texto_nome = fonte_pequena.render(f"Nome: {lista_rank[valor]}", True, BRANCO)
                        tela.blit(texto_nome, (nome.x, nome.y))
                        nome.y += 75
                    else:
                        texto_pontuacao = fonte_pequena.render(f"Pontuacao: {lista_rank[valor]}", True, BRANCO)
                        tela.blit(texto_pontuacao, (pontuacao.x, pontuacao.y))
                        pontuacao.y += 75
        lista = False

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False  
            
        pygame.display.flip()


def salvo(pontos):
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Salvar Ranking")
    fonte = pygame.font.SysFont("Arial", 48)
    fonte_pequena = pygame.font.SysFont("Arial", 32)
    box_nome = pygame.Rect(300,250,200,60)
    nome_escrita = ""
    
    rodando = True
    while rodando: 

        titulo = fonte.render(f"Nome", True, BRANCO)
        tela.blit(titulo, (LARGURA_TELA//2 - titulo.get_width()//2, 150))
        
        botao = pygame.Rect(300, 350, 200, 60)
        if nome_escrita != "":
            pygame.draw.rect(tela, AZUL, botao)
            texto_jogar = fonte_pequena.render("Salvar", True, BRANCO)
            tela.blit(texto_jogar, (botao.x + botao.width//2 - texto_jogar.get_width()//2,
                                    botao.y + botao.height//2 - texto_jogar.get_height()//2))
        else:
            pygame.draw.rect(tela, VERMELHO, botao)
            texto_jogar = fonte_pequena.render("Não salvar", True, BRANCO)
            tela.blit(texto_jogar, (botao.x + botao.width//2 - texto_jogar.get_width()//2,
                                    botao.y + botao.height//2 - texto_jogar.get_height()//2))
        

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False  
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao.collidepoint(evento.pos):
                    salvar_ranking(nome_escrita, CAMINHO_RANKING, pontos)
                    reordenar_ranking(CAMINHO_RANKING)
                    ranking()
                    rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    nome_escrita = nome_escrita[:-1]
                elif evento.key == pygame.K_RETURN or evento.key == pygame.K_SPACE:
                    nome_escrita = nome_escrita
                else:
                    nome_escrita += evento.unicode

        pygame.draw.rect(tela,(255,255,255),box_nome)

        nome = fonte_pequena.render(nome_escrita, True, (0,0,0))
        tela.blit(nome, (box_nome.x + 5, box_nome.y + 5))
        box_nome.w = max(50, nome.get_width() + 10)

        pygame.display.flip()