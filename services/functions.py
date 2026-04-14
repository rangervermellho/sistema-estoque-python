import json

from models.produto import Produto


def cadastro(lista_produto):
    """Função para cadastrar um novo produto, solicitando ao usuário o código, nome, preço e quantidade do produto."""

    while True:
        try:
            ##Verifica se o numero digitado é positivo ou negativo, e se o formato de entrada é valido, onde o código deve ser um número inteiro positivo, e caso o valor seja inválido,
            #  é exibida uma mensagem de erro e o usuário é solicitado a digitar novamente o código do produto. Além disso, é verificado se o código digitado já existe na lista de produtos cadastrados,
            #  e caso exista, é exibida uma mensagem informando que o código já existe e o usuário deve digitar um código diferente.
            codigo = int(input("Insira o código do produto: "))
            if codigo <= 0:
                print("O código deve ser maior que zero.")
                continue

            ##Verifica se o código digitado já existe na lista de produtos cadastrados, onde é utilizado uma expressão geradora para verificar se algum produto
            # na lista possui o mesmo código digitado pelo usuário. caso o código já exista, é exibida uma mensagem informando que o código já existe e o usuário deve
            # digitar um código diferente, e o loop continua solicitando um novo código.

            codigo_duplicado = any(p.codigo == codigo for p in lista_produto)
            if codigo_duplicado:
                print("Código já existe. Digite um código diferente.")
                continue

            break
        except ValueError:
            print("Valor inválido. Digite apenas números inteiros.")

    ##Entrada de nome do produto, String livre, sem validações especificas
    nome = str(input("Nome do Produto: "))

    while True:
        try:

            ##Entrada de quantidade com validação de numero positivo, e tratamento de erro para formato de entrada incorreto,
            # onde o valor deve ser um numero inteiro
            quantidade = int(input("Insira a quantidade: "))
            if quantidade < 0:
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
            if preco < 0:
                print("Valor nao deve ser negativo")
            else:

                break
        except ValueError:
            print("Valor inválido, formato de entrada R$ 00.00")

    ##Criação do objeto produto com os dados inseridos pelo usuário, e adição do produto na lista de produtos cadastrados

    novo_produto = Produto(codigo, nome, quantidade, preco)
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
    ##Função de busca de produto por nome
    nome = input("Insira o nome do produto: ").strip()
    ##Recebe o nome do digitado e busca na lista de cadastrados
    for p in lista_produto:
        if p.nome.lower() == nome.lower():
            print("produto encontrado ")
            p.mostrar()
            return p

    print("Produto não encontrado! ")
    return None


def editar_produto(lista_produto):
    ## Função para editar um produto cadastrado, onde o usuário é solicitado a inserir o código do produto que deseja editar,
    #  e caso o produto seja encontrado, é possível editar o nome, quantidade e preço do produto,
    #  com as mesmas validações de entrada utilizadas na função de cadastro. Caso o produto não seja encontrado,
    #  é exibida uma mensagem informando que o produto não foi encontrado.

    try:
        codigo = int(input("Código do produto que deseja editar: "))
    except ValueError:
        print("Digite um código válido.")
        return None
    for produto in lista_produto:
        if produto.codigo == codigo:
            print("Produto encontrado!")
            produto.mostrar()

            novo_nome = input("Novo nome do produto: ").strip()
            if novo_nome:
                produto.nome = novo_nome

            while True:
                try:
                    nova_quantidade = int(input("Nova quantidade: "))
                    if nova_quantidade < 0:
                        print("Quantidade não pode ser negativa.")
                    else:
                        produto.quantidade = nova_quantidade
                        break
                except ValueError:
                    print("Digite um número inteiro válido.")

            while True:
                try:
                    novo_preco = float(input("Novo valor: R$ "))
                    if novo_preco < 0:
                        print("Valor não pode ser negativo.")
                    else:
                        produto.preco = novo_preco
                        break
                except ValueError:
                    print("Digite um valor no formato 00.00")

            print("Produto atualizado com sucesso!")
            produto.mostrar()
            return produto

    print("Produto não encontrado.")
    return None


def excluir_produto(lista_produto):
    ##Função para excluir um produto cadastrado, onde o usuário é solicitado a inserir o código do produto que deseja excluir,
    #  e caso o produto seja encontrado, ele é removido da lista de produtos cadastrados.
    #  Caso o produto não seja encontrado, é exibida uma mensagem informando que o produto não foi encontrado.

    if len(lista_produto) == 0:
        print("Nenhum produto cadastrado! ")
        return

    try:
        codigo = int(input("Codigo do Produto que deseja excluir "))
    except ValueError:
        print("Digite um código válido.")
        return

    for p in lista_produto:
        if p.codigo == codigo:
            lista_produto.remove(p)
            print("Produto excluído!")
            return p

    print("Produto não encontrado! ")
    return None


def produto_mais_caro(lista_produto):
    ##Função para encontrar o produto mais caro, onde é verificado se a lista de produtos cadastrados está vazia, e caso esteja,
    #  é exibida uma mensagem informando que nenhum produto foi encontrado. Caso contrário,
    #  é percorrida a lista de produtos cadastrados para encontrar o produto com o maior preço,
    #  e em seguida, é exibida a informação do produto mais caro encontrado.

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
    ##Função para encontrar o produto com maior quantidade, onde é verificado se a lista de produtos cadastrados está vazia,
    #  e caso esteja, é exibida uma mensagem informando que nenhum produto foi encontrado. Caso contrário,
    #  é percorrida a lista de produtos cadastrados para encontrar o produto com a maior quantidade,.

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
    ##Função para calcular o valor total do estoque, onde é verificado se a lista de produtos cadastrados está vazia, e caso esteja,
    #  é exibida uma mensagem informando que nenhum produto foi encontrado. Caso contrário,
    #   é percorrida a lista de produtos cadastrados para calcular o valor total do estoque,
    # multiplicando o preço pela quantidade de cada produto, e em seguida, é exibida a soma total do estoque.

    total = sum(p.preco * p.quantidade for p in lista_produto)
    print(f"Valor total do estoque: R$ {total:.2f}")
    return total


def total_itens(lista_produto):
    ##Função para calcular o total de itens em estoque, onde é verificado se a lista de produtos cadastrados está vazia, e caso esteja,
    #  é exibida uma mensagem informando que nenhum produto foi encontrado. Caso contrário,
    #  é percorrida a lista de produtos cadastrados para calcular o total de itens em estoque,
    #  somando a quantidade de cada produto, e em seguida, é exibida a soma total de itens em estoque.

    total = sum(p.quantidade for p in lista_produto)
    print(f"Estoque total: {total} itens")
    return total


def salvar_estoque(lista_produtos):
    ##Função para salvar o estoque em um arquivo JSON, onde a lista de produtos cadastrados é convertida para um formato de dicionário utilizando
    #  o método to_dict() da classe Produto, e em seguida, é salvo em um arquivo chamado "estoque.json"
    #  utilizando a função json.dump(). O arquivo é salvo com indentação para facilitar a leitura,
    #  e o parâmetro ensure_ascii=False é utilizado para permitir a escrita de caracteres acentuados corretamente.
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            [p.to_dict() for p in lista_produtos], arquivo, indent=4, ensure_ascii=False
        )


def carregar_estoque():
    ##Função para carregar o estoque a partir de um arquivo JSON, onde é verificado se o arquivo "estoque.json" existe, e caso exista,
    #  o conteúdo do arquivo é lido e convertido para uma lista de objetos Produto utilizando o método from_dict() da classe Produto.
    #  Caso o arquivo não exista, é retornada uma lista vazia, indicando que nenhum produto foi carregado.
    try:
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return [Produto.from_dict(p) for p in dados]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao carregar o estoque. O arquivo está corrompido.")
        return []
