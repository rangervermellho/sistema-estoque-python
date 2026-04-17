class Produto:
    def __init__(self, codigo: int, nome: str, quantidade: int, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def mostrar(self) -> None:
        print(
            f"\nCódigo do Produto: {self.codigo} | "
            f"Nome do Produto: {self.nome} | "
            f"Quantidade: {self.quantidade} | "
            f"Preço: R$ {self.preco:.2f}"
        )

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco,
        }

    @classmethod
    def from_dict(cls, dados: dict):
        return cls(
            codigo=dados["codigo"],
            nome=dados["nome"],
            quantidade=dados["quantidade"],
            preco=dados["preco"],
        )
