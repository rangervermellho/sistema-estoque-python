from models.produto import Produto
from services.estoque_service import (
    cadastrar_produto,
    buscar_por_codigo,
    excluir_produto,
)
from services.relatorios_service import produto_mais_caro


def test_cadastrar_produto_com_codigo_unico():
    produtos = []
    produto = Produto(1, "Teclado", 2, 100.0)

    resultado = cadastrar_produto(produtos, produto)

    assert resultado is True
    assert len(produtos) == 1


def test_nao_cadastra_codigo_duplicado():
    produtos = [Produto(1, "Teclado", 2, 100.0)]
    novo = Produto(1, "Mouse", 1, 50.0)

    resultado = cadastrar_produto(produtos, novo)

    assert resultado is False
    assert len(produtos) == 1


def test_buscar_por_codigo():
    produtos = [Produto(1, "Teclado", 2, 100.0)]

    resultado = buscar_por_codigo(produtos, 1)

    assert resultado is not None
    assert resultado.nome == "Teclado"


def test_excluir_produto():
    produtos = [Produto(1, "Teclado", 2, 100.0)]

    resultado = excluir_produto(produtos, 1)

    assert resultado is True
    assert len(produtos) == 0


def test_produto_mais_caro():
    produtos = [
        Produto(1, "Teclado", 2, 100.0),
        Produto(2, "Monitor", 1, 900.0),
    ]

    resultado = produto_mais_caro(produtos)

    assert resultado is not None
    assert resultado.nome == "Monitor"