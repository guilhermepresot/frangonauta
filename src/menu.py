import pygame

def menu():
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Menu")
    fonte = pygame.font.SysFont("Arial", 48)
    fonte_pequena = pygame.font.SysFont("Arial", 32)
    
    rodando = True
    while rodando: 

        titulo = fonte.render("FRANGONAUTA", True, (255, 255, 255))
        tela.blit(titulo, (800//2 - titulo.get_width()//2, 150))

        
        botao = pygame.Rect(300, 300, 200, 60)
        pygame.draw.rect(tela, (0, 200, 0), botao)
        texto_jogar = fonte_pequena.render("JOGAR", True, (255, 255, 255))
        tela.blit(texto_jogar, (botao.x + botao.width//2 - texto_jogar.get_width()//2,
                                botao.y + botao.height//2 - texto_jogar.get_height()//2))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False  
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao.collidepoint(evento.pos):
                    return True  

        pygame.display.flip()