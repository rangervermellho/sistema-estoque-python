def ler_int_positivo(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_int_nao_negativo(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_float_nao_negativo(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("Digite um valor numérico válido.")