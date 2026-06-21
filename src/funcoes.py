import random
import pygame

def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos

def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano

def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0

def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)
   
def aleatorizar_posicao(elemento, altura, gerador):
    elemento.y = gerador(0, altura)

def criar_objeto(lista, imagem, function, altura, gerador=random.randint):
    objeto = function(imagem)
    aleatorizar_posicao(objeto, altura, gerador)
    lista.append(objeto)

def movimentacao_jogador(velocidade_y, jogador):
    """Seção da movimentação do frango"""
    jogador.y += velocidade_y

def movimentacao_objeto(lista, velocidade_x):
    """Seção da movimentação dos objetos"""
    for objeto in lista:
        objeto.x += velocidade_x

def exibe_mensagem(msg, tamanho, cor):
    """Exibe uma mensagem na tela padronizada"""
    fonte = pygame.font.SysFont("Arial", tamanho, True, False)
    mensagem = f'{msg}'
    texto_formato = fonte.render(mensagem, True, cor)
    return texto_formato

def tamanho_texto(lista):
    """Informa o tamanho do parâmetro"""
    return len(lista)