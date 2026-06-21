import pygame
from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    TITULO_JOGO,
    AZUL,
    VERDE,
    BRANCO
)

def menu(recorde):
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Menu")
    fonte = pygame.font.SysFont("Arial", 48)
    fonte_pequena = pygame.font.SysFont("Arial", 32)
    
    rodando = True
    while rodando: 

        titulo = fonte.render(f"{TITULO_JOGO}", True, BRANCO)
        tela.blit(titulo, (LARGURA_TELA//2 - titulo.get_width()//2, 150))
        
        botao = pygame.Rect(300, 250, 200, 60)
        pygame.draw.rect(tela, AZUL, botao)
        texto_jogar = fonte_pequena.render("JOGAR", True, BRANCO)
        tela.blit(texto_jogar, (botao.x + botao.width//2 - texto_jogar.get_width()//2,
                                botao.y + botao.height//2 - texto_jogar.get_height()//2))
        
        recorde_menu = pygame.Rect(300, 350, 200, 60)
        pygame.draw.rect(tela, VERDE, recorde_menu)
        texto_recorde = fonte_pequena.render(f"Recorde: {recorde}", True, BRANCO)
        tela.blit(texto_recorde, (recorde_menu.x + recorde_menu.width//2 - texto_recorde.get_width()//2,
                                recorde_menu.y + recorde_menu.height//2 - texto_recorde.get_height()//2))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False  
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao.collidepoint(evento.pos):
                    return True  

        pygame.display.flip()