import json
from models.produto import Produto


def cadastro(lista_produto):
    nome = str(input("Nome do Produto: " ))

    while True:
        try: 
            preco = float(input("Valor do item: R$ "))
            break
        except ValueError:
            print("Valor inválido, formato de entrada R$ 00.00")
        

    while True:
        try:
            quantidade = int(input("Insira a quantidade: "))
            break
        except ValueError:
            print("Valor Inválido")

    
    novo_produto = Produto(nome, preco, quantidade)
    lista_produto.append(novo_produto)
    print(f" Produto '{nome}' cadastrado!")


def produtos_cadastrados(lista_produto):
    if len(lista_produto) == 0:
        print("Nenhum produto cadastrado! ")
    else:
        print("Produtos cadastrados")
    for p in lista_produto:
        p.mostrar()


def buscar(lista_produto):
    nome = input("Qual produto deseja buscar")

    for p in lista_produto:
        if p.nome.lower() == nome.lower():
            print("produto encontrado ")
            p.mostrar()
            return p
    
    print("Produto não encontrado! ")
    return None


def editar_produto(lista_produto):
    nome = input("Nome do produto que deseja editar: ")    

    for p in lista_produto:
        if p.nome.lower() == nome.lower():
            novo_nome = input("Novo nome: ")
            try:
                novo_valor = float(input("Novo Valor: R$ "))
            except ValueError:
                print("valor incorreto, digite preço valido")
                return
            
            p.nome = novo_nome
            p.valor = novo_valor
            print("Produto atualizado! ")
            p.mostrar()
            return p
    
    print("produto não encontrado")


def excluir_produto(lista_produto):
    for p in lista_produto:
        p.mostrar()

    nome = input("Nome do Produto que deseja excluir ")

    for p in lista_produto:
        if p.nome.lower() == nome.lower():
            lista_produto.remove(p)
            print("Produto excluído!")
            return p
    
    print("Produto não encontrado! ")
    return None


def produto_mais_caro(lista_produto):
    if len(lista_produto) == 0:
        print("Nenhum produto encontrado")
        return
    
    mais_caro = lista_produto[0]

    for p in lista_produto:
        if p.preco > mais_caro.preco:
            mais_caro = p
    
        print("Produto mais caro é :")
        mais_caro.mostrar()


def produto_maior_quantia(lista_produto):
    if len(lista_produto) == 0:
        print("Nenhum produto encontrado ")
        return
    
    quant_itens = lista_produto[0]
    
    for p in lista_produto:
        if p.quantidade > quant_itens:
            quant_itens = p

        print("Produto com maior quantidade é: ")
        quant_itens.mostrar()


def valor_estoque(lista_produto):
   total = sum(p.preco * p.quantidade for p in lista_produto)
   print(f"Soma total do estoque é : R$ {total:.2f}")
   return total


def total_itens(lista_produto):
    total = sum(p.quantidade for p in lista_produto )
    print(f"estoque total é de {total:.2f} itens")
    return total


def salvar_estoque(lista_produtos):
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump([p.to_dict() for p in lista_produtos], arquivo, indent=4, ensure_ascii=False)


def carregar_estoque():

    try:
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            dados =json.load(arquivo)
        return[Produto.from_dict(p) for p in dados]
    except FileNotFoundError:
        return []

