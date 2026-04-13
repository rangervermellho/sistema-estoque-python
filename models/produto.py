import json

class Produto:

    def __init__ (self, cod_produto, nome, quantidade, preco):
        self.codigo = cod_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco    


    def mostrar(self):
        print(f"\nCodigo do Produto: {self.codigo} | Nome do Produto: {self.nome} | Quantidade: {self.quantidade} | Preço: R$ {self.preco:.2f}")


    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco
        }
    
    @staticmethod
    def from_dict(dados):
        return Produto(
            cod_produto=dados["codigo"],
            nome=dados["nome"],
            quantidade=dados["quantidade"],
            preco=dados["preco"]
        )