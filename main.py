from services.functions import cadastro, produtos_cadastrados, buscar, editar_produto, excluir_produto, produto_mais_caro, produto_maior_quantia, valor_estoque, total_itens, salvar_estoque, carregar_estoque
import json


lista_produto = carregar_estoque()

while True:
    print("\n ===  SISTEMA DE CONTROLE ESTOQUE ===\n")
    print("1 - Cadastrar produto")
    print("2 - Produtos cadastrados")
    print("3 - Buscar produto")
    print("4 - Editar cadastro")
    print("5 - Excluir produto")
    print("6 - Produto mais caro")
    print("7 - Produto com maior quantidade")
    print("8 - Valor total em estoque")
    print("9 - Total de itens em estoque")
    print("10 - Salvar e sair\n")


    try:
        menu = int(input("\nEscolha uma opção: \n"))
    except ValueError:
        print("Escolha uma das opções validas")
        continue
    if menu == 1:
        cadastro(lista_produto)
    elif menu == 2:
        produtos_cadastrados(lista_produto)
    elif menu == 3:
        buscar(lista_produto)
    elif menu == 4:
        editar_produto(lista_produto)
    elif menu == 5:
        excluir_produto(lista_produto)
    elif menu == 6:
        produto_mais_caro(lista_produto)
    elif menu == 7:
        produto_maior_quantia(lista_produto)
    elif menu == 8:
        valor_estoque(lista_produto)
    elif menu == 9:
        total_itens(lista_produto)
    elif menu == 10:
        salvar_estoque(lista_produto)
        print("Salvando e saindo...")
        break
    else:
        print("Opção inválida. ")



