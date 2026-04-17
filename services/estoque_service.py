from models.produto import Produto


def codigo_existe(lista_produtos: list[Produto], codigo: int) -> bool:
    return any(p.codigo == codigo for p in lista_produtos)


def buscar_por_codigo(lista_produtos: list[Produto], codigo: int) -> Produto | None:
    for produto in lista_produtos:
        if produto.codigo == codigo:
            return produto
    return None


def buscar_por_nome(lista_produtos: list[Produto], nome: str) -> Produto | None:
    nome = nome.strip().lower()
    for produto in lista_produtos:
        if produto.nome.lower() == nome:
            return produto
    return None


def cadastrar_produto(lista_produtos: list[Produto], produto: Produto) -> bool:
    if codigo_existe(lista_produtos, produto.codigo):
        return False
    lista_produtos.append(produto)
    return True


def excluir_produto(lista_produtos: list[Produto], codigo: int) -> bool:
    produto = buscar_por_codigo(lista_produtos, codigo)
    if not produto:
        return False
    lista_produtos.remove(produto)
    return True