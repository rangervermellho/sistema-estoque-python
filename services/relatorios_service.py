from models.produto import Produto


def produto_mais_caro(lista_produtos: list[Produto]) -> Produto | None:
    if not lista_produtos:
        return None
    return max(lista_produtos, key=lambda p: p.preco)


def produto_maior_quantidade(lista_produtos: list[Produto]) -> Produto | None:
    if not lista_produtos:
        return None
    return max(lista_produtos, key=lambda p: p.quantidade)


def valor_estoque(lista_produtos: list[Produto]) -> float:
    return sum(p.preco * p.quantidade for p in lista_produtos)


def total_itens(lista_produtos: list[Produto]) -> int:
    return sum(p.quantidade for p in lista_produtos)