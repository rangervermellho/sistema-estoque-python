import json
##classe Produto, onde são definidos os atributos do produto, como código, nome, quantidade e preço,
#  e métodos para mostrar as informações do produto, converter o produto para um dicionário e criar um produto a
#  partir de um dicionário. A classe é utilizada para representar os produtos cadastrados no sistema de controle de estoque.

class Produto:
    
## função de inicialização da classe Produto, onde são definidos os atributos do produto, como código, nome, quantidade e preço.
#  O método __init__ é chamado quando um objeto da classe Produto é criado, e os valores dos atributos são passados como
#  parâmetros para a função.

    def __init__ (self, cod_produto, nome, quantidade, preco):
        self.codigo = cod_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco    

## método para mostrar as informações do produto, onde as informações do produto são exibidas de forma formatada,
#  incluindo o código, nome, quantidade e preço do produto. O método mostrar() é utilizado para exibir as informações
#  de um produto específico quando necessário.

    def mostrar(self):
        print(f"\nCodigo do Produto: {self.codigo} | Nome do Produto: {self.nome} | Quantidade: {self.quantidade} | Preço: R$ {self.preco:.2f}")

## método para converter o produto para um dicionário, onde os atributos do produto são convertidos para um formato de dicionário,
#  com as chaves correspondentes aos nomes dos atributos. O método to_dict() é utilizado para facilitar a conversão dos objetos Produto 
# para um formato que pode ser facilmente salvo em um arquivo JSON.

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco
        }
## método estático para criar um produto a partir de um dicionário, onde os valores do dicionário são utilizados para criar um objeto da classe Produto.
# O método from_dict() é utilizado para facilitar a criação de objetos Produto a partir de dados carregados de um arquivo JSON,
# onde os dados são lidos como dicionários e precisam ser convertidos para objetos da classe Produto para serem utilizados no sistema de controle de estoque.

    @staticmethod
    def from_dict(dados):
        return Produto(
            cod_produto=dados["codigo"],
            nome=dados["nome"],
            quantidade=dados["quantidade"],
            preco=dados["preco"]
        )