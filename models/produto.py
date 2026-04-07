import json

class Produto:

    def __init__ (self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco    


    def mostrar(self):
        print(f"\nNome do Produto: {self.nome} | Quantidade: {self.quantidade} | Preço: R$ {self.preco:.2f}")


    def to_dict(self):
        return {
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco
        }
    

    def from_dict(dados):
        return Produto(
            nome=dados["nome"],
            quantidade=dados["quantidade"],
            preco=dados["preco"]
        )