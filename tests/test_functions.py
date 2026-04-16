from models.produto import Produto
from services.functions import valor_estoque, total_itens


def test_valor_estoque():
    produtos = [
        Produto(1, "Teclado", 2, 100.0),
        Produto(2, "Mouse", 3, 50.0),
    ]

    resultado = valor_estoque(produtos)
    assert resultado == 350.0


def test_total_itens():
    produtos = [
        Produto(1, "Teclado", 2, 100.0),
        Produto(2, "Mouse", 3, 50.0),
    ]

    resultado = total_itens(produtos)
    assert resultado == 5