from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    verificar_colisao,
    tomar_dano,
    criar_objeto,
    movimentacao_jogador,
    movimentacao_objeto,
    tamanho_texto
)


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_dano_correto():
    """Deve indicar corretamente o dano recebido pelo jogador."""
    assert tomar_dano(3, 1) == 2


def test_calcular_tamanho():
    """Deve indicar corretamente o tamanho do parâmetro"""
    assert tamanho_texto("aaa") == 3

def test_verificar_colisao_quando_ha_sobreposicao():
    """Deve indicar corretamente quando dois objetos colidem."""
    objeto_1 = lambda: None
    objeto_1.x, objeto_1.y, objeto_1.width, objeto_1.height = 0, 0, 50, 50

    objeto_2 = lambda: None
    objeto_2.x, objeto_2.y, objeto_2.width, objeto_2.height = 25, 25, 50, 50

    objeto_1.colliderect = lambda outro: (
        objeto_1.x < outro.x + outro.width and objeto_1.x + objeto_1.width > outro.x
        and objeto_1.y < outro.y + outro.height and objeto_1.y + objeto_1.height > outro.y
    )

    assert verificar_colisao(objeto_1, objeto_2) is True


def test_verificar_colisao_sem_sobreposicao():
    """Deve indicar corretamente quando dois objetos não colidem."""
    objeto_1 = lambda: None
    objeto_1.x, objeto_1.y, objeto_1.width, objeto_1.height = 0, 0, 50, 50

    objeto_2 = lambda: None
    objeto_2.x, objeto_2.y, objeto_2.width, objeto_2.height = 200, 200, 50, 50

    objeto_1.colliderect = lambda outro: (
        objeto_1.x < outro.x + outro.width and objeto_1.x + objeto_1.width > outro.x
        and objeto_1.y < outro.y + outro.height and objeto_1.y + objeto_1.height > outro.y
    )

    assert verificar_colisao(objeto_1, objeto_2) is False


def test_movimentacao_jogador_atualiza_posicao():
    """Deve mover o jogador verticalmente conforme a velocidade."""
    jogador = lambda: None
    jogador.x, jogador.y = 0, 100
    movimentacao_jogador(10, jogador)
    assert jogador.y == 110


def test_movimentacao_objeto_move_todos_os_itens():
    """Deve mover todos os objetos da lista horizontalmente."""
    objeto_1 = lambda: None
    objeto_1.x, objeto_1.y = 100, 0

    objeto_2 = lambda: None
    objeto_2.x, objeto_2.y = 200, 0

    lista = [objeto_1, objeto_2]
    movimentacao_objeto(lista, -10)
    assert objeto_1.x == 90
    assert objeto_2.x == 190


def test_criar_objeto_adiciona_na_lista():
    """Deve adicionar um novo objeto à lista de objetos do jogo."""
    lista = []
    gerador_fixo = lambda minimo, maximo: 42

    def criar_objeto_falso(imagem):
        objeto = lambda: None
        objeto.x, objeto.y, objeto.img = 0, 0, imagem
        return objeto

    criar_objeto(lista, "imagem_falsa", criar_objeto_falso, 500, gerador=gerador_fixo)
    assert len(lista) == 1
    assert lista[0].y == 42