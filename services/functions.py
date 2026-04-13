import json
from models.produto import Produto


def cadastro(lista_produto):

    '''Função para cadastrar um novo produto, solicitando ao usuário o código, nome, preço e quantidade do produto.'''
    
    while True:
        try:

            ##Validação de numero positivo para o codigo do produto
            codigo = int(input("Insira o codigo do produto: "))

            if codigo <= 0 :
                print("Codigo nao pode ser negativo!")
                continue

            ##Validação de codigo unico por produto, verificando se o codigo ja existe na lista de produtos cadastrados
            cod_existe = False
            for c in lista_produto:
                if c.codigo == codigo:
                    cod_existe = True
                    print("Codigo já existe, insira um codigo diferente! ")
                    break

            else:
                break
        except ValueError:
            print("Valor invalido, somente numeros inteiros")

    ##Entrada de nome do produto, String livre, sem validações especificas
    nome = str(input("Nome do Produto: " ))

    while True:
        try:

            ##Entrada de quantidade com validação de numero positivo, e tratamento de erro para formato de entrada incorreto, 
            # onde o valor deve ser um numero inteiro
            quantidade = int(input("Insira a quantidade: "))
            if quantidade < 0 :
                print("Valor não deve ser negativo")
            else:   
                break
        except ValueError:
            print("Valor Inválido")

    while True:
        try:
            ##Entrada de preço com validação de numero postivo, e tratamento de erro para formato de entrada incorreto, 
            # onde o valor deve ser digitado no formato R$ 00.00 
            preco = float(input("Valor do item: R$ "))
            if preco < 0 :
                print("Valor nao deve ser negativo")
            else:

                break
        except ValueError:
            print("Valor inválido, formato de entrada R$ 00.00")
        


    ##Criação do objeto produto com os dados inseridos pelo usuário, e adição do produto na lista de produtos cadastrados

    novo_produto = Produto(codigo, nome, quantidade, preco )
    lista_produto.append(novo_produto)
    print(f" Produto '{nome}' cadastrado!")


def produtos_cadastrados(lista_produto):
##Função para exibir os produtos cadastrados, onde é verificado se a lista de produtos está vazia, e caso esteja,
#  é exibida uma mensagem informando que nenhum produto foi cadastrado. Caso contrário, é exibida a lista de produtos cadastrados
#  exibindo as informações de cada produto.

    if len(lista_produto) == 0:
        print("Nenhum produto cadastrado! ")
    else:
        print("Produtos cadastrados")
    for p in lista_produto:
        p.mostrar()


def buscar(lista_produto):
##Funçao de busca de produto por nome 
    print("Insira Nome do produto\n")

    nome=input()

##Recebe o nome do digitado e busca na lista de cadastrados

    for p in lista_produto:
        if p.nome.lower() == nome.lower():
            print("produto encontrado ")
            p.mostrar()
            return p
    
        else:
            print("Produto não encontrado! ")
            return None


def editar_produto(lista_produto):
    try:
        codigo = int(input("Codigo do produto que deseja editar: "))
    except ValueError:
        print("Digite um código válido.")
        return

    for p in lista_produto:
        if p.codigo == codigo:
            print("Produto encontrado!")
            p.mostrar()

            novo_nome = input("Novo nome do produto: ")

            while True:
                try:
                    novo_preco = float(input("Novo valor: R$ "))
                    if novo_preco < 0:
                        print("Valor não pode ser negativo.")
                    else:
                        break
                except ValueError:
                    print("Valor digitado deve ser no formato 00.00")

            while True:
                try:
                    nova_quantidade = int(input("Nova quantidade: "))
                    if nova_quantidade < 0:
                        print("Quantidade não pode ser negativa.")
                    else:
                        break
                except ValueError:
                    print("Digite um número inteiro válido.")

            p.nome = novo_nome
            p.preco = novo_preco
            p.quantidade = nova_quantidade

            print("Produto atualizado!")
            p.mostrar()
            return p

    print("Produto não encontrado.")
    
    print("produto não encontrado")


def excluir_produto(lista_produto):
    for p in lista_produto:
        p.mostrar()
    
    codigo = int(input("Codigo do Produto que deseja excluir "))

    for p in lista_produto:
        if p.codigo == codigo:
            lista_produto.remove(p)
            print("Produto excluído!")
            return p
        
        else:
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
    
    maior_produto = lista_produto[0]
    
    for p in lista_produto:
        if p.quantidade > maior_produto.quantidade:
            maior_produto = p

    print("Produto com maior quantidade é: ")
    maior_produto.mostrar()


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
            dados=json.load(arquivo)
        return[Produto.from_dict (p) for p in dados]
    except FileNotFoundError:
        return []

