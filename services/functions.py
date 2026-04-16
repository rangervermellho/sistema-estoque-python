import json

from models.produto import Produto


def cadastro(lista_produto):
    ##cadasto de produtos, verificando se o codigo é unico e se os valores são validos
    while True:
        try:
            codigo = int(input("Insira o código do produto: "))
            if codigo <= 0:
                print("O código deve ser maior que zero.")
                continue


            codigo_duplicado = any(p.codigo == codigo for p in lista_produto)
            if codigo_duplicado:
                print("Código já existe. Digite um código diferente.")
                continue

            break
        except ValueError:
            print("Valor inválido. Digite apenas números inteiros.")

  
    nome = str(input("Nome do Produto: "))

    while True:
        try:

        
            quantidade = int(input("Insira a quantidade: "))
            if quantidade < 0:
                print("Valor não deve ser negativo")
            else:
                break
        except ValueError:
            print("Valor Inválido")

    while True:
        try:
           
            preco = float(input("Valor do item: R$ "))
            if preco < 0:
                print("Valor nao deve ser negativo")
            else:

                break
        except ValueError:
            print("Valor inválido, formato de entrada R$ 00.00")

    
    novo_produto = Produto(codigo, nome, quantidade, preco)
    lista_produto.append(novo_produto)
    print(f" Produto '{nome}' cadastrado!")


def produtos_cadastrados(lista_produto):
    ##mostra todos produtos cadastrados, caso nao haja nenhum produto, mostra mensagem de aviso
    if len(lista_produto) == 0:
        print("Nenhum produto cadastrado! ")
    else:
        print("Produtos cadastrados")
    for p in lista_produto:
        p.mostrar()


def buscar(lista_produto):
    ##Busca produtos pelo nome, caso nao haja nenhum produto, mostra mensagem de aviso
    nome = input("Insira o nome do produto: ").strip()
    
    for p in lista_produto:
        if p.nome.lower() == nome.lower():
            print("produto encontrado ")
            p.mostrar()
            return p

    print("Produto não encontrado! ")
    return None


def editar_produto(lista_produto):
   ##edita lista de produto com base no codigo do produto
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
    ##exclui o produti com base no codigo do produto
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
##percorre a lista de produtos e retorna o produto com maior valor
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
   ##percorre a lista e retorna o produto com maior qusntidade em estoque
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
##soma o valor de todos os itens do estoque e retorna o valor total do estoque
    total = sum(p.preco * p.quantidade for p in lista_produto)
    print(f"Valor total do estoque: R$ {total:.2f}")
    return total


def total_itens(lista_produto):
##soma todos os itens do estoque. retorna o  total de itens em estoque
    total = sum(p.quantidade for p in lista_produto)
    print(f"Estoque total: {total} itens")
    return total


def salvar_estoque(lista_produtos):
    ##salva a lista em arquivo JSON, convertendo os objetos Produto em dicionários usando o método to_dict()
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            [p.to_dict() for p in lista_produtos], arquivo, indent=4, ensure_ascii=False
        )


def carregar_estoque():
    ##carrga a lista de produtos do arquivo JSON
    try:
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return [Produto.from_dict(p) for p in dados]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao carregar o estoque. O arquivo está corrompido.")
        return []




