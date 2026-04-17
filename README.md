# Sistema de Controle de Estoque em Python

Projeto desenvolvido com foco na prática de desenvolvimento back-end utilizando Python.

Este sistema simula um controle de estoque completo via terminal (CLI), permitindo o gerenciamento de produtos com persistência de dados e aplicação de boas práticas de desenvolvimento.

---

## Status do Projeto

 Em desenvolvimento ativo
 Projeto em evolução contínua

---

## Funcionalidades

* Cadastro de produtos
* Listagem de produtos
* Busca por nome e código
* Edição de produtos
* Exclusão de produtos

### Relatórios

* Produto mais caro
* Produto com maior quantidade
* Valor total em estoque
* Total de itens

 Persistência de dados utilizando JSON

---

## Tecnologias utilizadas

* Python 3
* JSON (persistência de dados)
* Pytest (testes automatizados)

 **Conceitos aplicados:**

* Programação Orientada a Objetos (POO)
* Separação de responsabilidades
* Modularização de código
* Validação de dados
* Estrutura em camadas (models, services, utils)

---

## Estrutura do projeto

```text
sistema-estoque-python/
│
├── models/            # Classes do sistema (Produto)
├── services/          # Regras de negócio
├── utils/             # Funções auxiliares (validações, inputs)
├── tests/             # Testes automatizados
│
├── main.py            # Arquivo principal (menu e fluxo)
├── requirements.txt   # Dependências do projeto
├── .gitignore         # Arquivos ignorados pelo Git
└── README.md          # Documentação do projeto
```

---

## Exemplo de uso

```text
=== SISTEMA DE CONTROLE DE ESTOQUE ===

1 - Cadastrar produto
2 - Listar produtos
3 - Buscar produto
4 - Editar produto
5 - Excluir produto
6 - Produto mais caro
7 - Produto com maior quantidade
8 - Valor total em estoque
9 - Total de itens
10 - Salvar e sair

Escolha uma opção: 1

Código: 1
Nome: Teclado
Quantidade: 10
Preço: 100

Produto cadastrado com sucesso!
```

---

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/rangervermellho/sistema-estoque-python.git
```

1. Acesse a pasta do projeto:

```bash
cd sistema-estoque-python
```

1. Execute o sistema:

```bash
python main.py
```

---

## Como rodar os testes

Instale as dependências (caso necessário):

```bash
pip install -r requirements.txt
```

Execute os testes com:

```bash
pytest
```

---

## Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de evoluir habilidades em:

* Desenvolvimento back-end com Python
* Programação Orientada a Objetos (POO)
* Organização e modularização de código
* Boas práticas de desenvolvimento
* Escrita de testes automatizados

---

## Objetivo profissional

Este projeto faz parte da minha jornada de evolução como Desenvolvedor Python, com foco em aplicar boas práticas e me preparar para atuar profissionalmente na área.

---

## Próximas melhorias

* Implementação de interface gráfica ou API
* Sistema de autenticação (login)
* Integração com banco de dados
* Melhor cobertura de testes

---

## Autor

Desenvolvido por Eduardo Neri

🔗 LinkedIn: <https://www.linkedin.com/in/eduardo-neri-96b3732a5/>
🔗 GitHub: <https://github.com/rangervermellho>
