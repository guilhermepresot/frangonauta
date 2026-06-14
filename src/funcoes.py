import random

def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)
    
def aleatorizar_posicao(elemento, altura, gerador):
    elemento.y = gerador(0, altura)

def criar_objeto(lista, imagem, function, altura, gerador=random.randint):
    objeto = function(imagem)
    aleatorizar_posicao(objeto, altura, gerador)
    lista.append(objeto)

def movimentacao(lista, velocidade_x, velocidade_y, largura, jogador):
    #seção da movimentação do meteoro
    for meteoro in lista:
        meteoro.x += velocidade_x
    while len(lista) > 0 and lista[0].x + largura < 0:
        lista.pop(0) #salva memoria de ser gasta com obstáculos antigos

    #seção da movimentação do frango
    jogador.y += velocidade_y

def movimentacao_batata(lista, velocidade_x):
    #seção da movimentação da batata
    for meteoro in lista:
        meteoro.x += velocidade_x