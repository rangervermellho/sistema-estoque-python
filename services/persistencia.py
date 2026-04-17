import json
from models.produto import Produto

ARQUIVO_ESTOQUE = "estoque.json"


def salvar_estoque(lista_produtos: list[Produto]) -> None:
    with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as arquivo:
        json.dump(
            [p.to_dict() for p in lista_produtos],
            arquivo,
            indent=4,
            ensure_ascii=False,
        )


def carregar_estoque() -> list[Produto]:
    try:
        with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return [Produto.from_dict(item) for item in dados]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao carregar o estoque. O arquivo está corrompido.")
        return []