import pygame
            
def pegar_sprite(local_arquivo, x, y, width, height, scale=1):
    """Corta um único elemento de uma spritesheet e remove o fundo."""
    
    sheet = pygame.image.load(local_arquivo)
    
    # Se a imagem tiver transparência (PNG), usa convert_alpha
    if sheet.get_masks()[3] != 0:
        sheet = sheet.convert_alpha()
        image = pygame.Surface((width, height), pygame.SRCALPHA)
    else:
        sheet = sheet.convert()
        image = pygame.Surface((width, height))
        
    image.blit(sheet, (0, 0), (x, y, width, height))
    
    # Remove fundo apenas para imagens sem alpha (BMP)
    if not (sheet.get_masks()[3] != 0):
        cor_do_fundo = image.get_at((0, 0))
        image.set_colorkey(cor_do_fundo)
    
    if scale != 1:
        novo_largura = int(width * scale)
        novo_altura = int(height * scale)
        image = pygame.transform.scale(image, (novo_largura, novo_altura))
        
    return image