from models.produto import Produto
from services.estoque_service import (
    cadastrar_produto,
    buscar_por_codigo,
    buscar_por_nome,
    excluir_produto,
)
from services.relatorios_service import (
    produto_mais_caro,
    produto_maior_quantidade,
    valor_estoque,
    total_itens,
)
from services.persistencia import salvar_estoque, carregar_estoque
from utils.inputs import ler_int_positivo, ler_int_nao_negativo, ler_float_nao_negativo


def exibir_menu() -> None:
    print("\n=== SISTEMA DE CONTROLE DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto por nome")
    print("4 - Editar produto")
    print("5 - Excluir produto")
    print("6 - Produto mais caro")
    print("7 - Produto com maior quantidade")
    print("8 - Valor total em estoque")
    print("9 - Total de itens")
    print("10 - Salvar e sair")


def listar_produtos(lista_produtos):
    if not lista_produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in lista_produtos:
        produto.mostrar()


def main():
    lista_produtos = carregar_estoque()

    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite uma opção válida.")
            continue

        if opcao == 1:
            codigo = ler_int_positivo("Código: ")
            nome = input("Nome: ").strip()
            quantidade = ler_int_nao_negativo("Quantidade: ")
            preco = ler_float_nao_negativo("Preço: R$ ")

            produto = Produto(codigo, nome, quantidade, preco)
            if cadastrar_produto(lista_produtos, produto):
                print("Produto cadastrado com sucesso!")
            else:
                print("Já existe um produto com esse código.")

        elif opcao == 2:
            listar_produtos(lista_produtos)

        elif opcao == 3:
            nome = input("Nome do produto: ")
            produto = buscar_por_nome(lista_produtos, nome)
            if produto:
                produto.mostrar()
            else:
                print("Produto não encontrado.")

        elif opcao == 4:
            codigo = ler_int_positivo("Código do produto: ")
            produto = buscar_por_codigo(lista_produtos, codigo)

            if not produto:
                print("Produto não encontrado.")
                continue

            novo_nome = input("Novo nome: ").strip()
            if novo_nome:
                produto.nome = novo_nome

            produto.quantidade = ler_int_nao_negativo("Nova quantidade: ")
            produto.preco = ler_float_nao_negativo("Novo preço: R$ ")
            print("Produto atualizado com sucesso!")

        elif opcao == 5:
            codigo = ler_int_positivo("Código do produto: ")
            if excluir_produto(lista_produtos, codigo):
                print("Produto excluído com sucesso!")
            else:
                print("Produto não encontrado.")

        elif opcao == 6:
            produto = produto_mais_caro(lista_produtos)
            if produto:
                produto.mostrar()
            else:
                print("Nenhum produto cadastrado.")

        elif opcao == 7:
            produto = produto_maior_quantidade(lista_produtos)
            if produto:
                produto.mostrar()
            else:
                print("Nenhum produto cadastrado.")

        elif opcao == 8:
            print(f"Valor total em estoque: R$ {valor_estoque(lista_produtos):.2f}")

        elif opcao == 9:
            print(f"Total de itens: {total_itens(lista_produtos)}")

        elif opcao == 10:
            salvar_estoque(lista_produtos)
            print("Salvando e saindo...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()