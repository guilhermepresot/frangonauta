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