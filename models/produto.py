class Produto:
    def __init__(self, cod_produto: int, nome: str, quantidade: int, preco: float):
        self.codigo = cod_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def mostrar(self):
        print(
            f"\nCódigo do Produto: {self.codigo} | "
            f"Nome do Produto: {self.nome} | "
            f"Quantidade: {self.quantidade} | "
            f"Preço: R$ {self.preco:.2f}"
        )

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco,
        }

    @staticmethod
    def from_dict(dados):
        return Produto(
            cod_produto=dados["codigo"],
            nome=dados["nome"],
            quantidade=dados["quantidade"],
            preco=dados["preco"],
        )
