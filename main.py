import json
import os

ARQUIVO = "dados.json"


def carregar_dados():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            print("Não foi possível ler os dados. Começando com a lista vazia.")
    return []


def salvar_dados(produtos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, ensure_ascii=False, indent=4)


def proximo_id(produtos):
    if len(produtos) == 0:
        return 1
    return max(produto["id"] for produto in produtos) + 1


def incluir(produtos):
    print("\n--- INCLUIR PRODUTO ---")
    nome = input("Nome: ").strip()
    categoria = input("Categoria: ").strip()
    descricao = input("Descrição: ").strip()

    if nome == "" or categoria == "":
        print("Nome e categoria são obrigatórios.")
        return

    produto = {
        "id": proximo_id(produtos),
        "nome": nome,
        "categoria": categoria,
        "descricao": descricao
    }

    produtos.append(produto)
    salvar_dados(produtos)
    print("Produto cadastrado com sucesso!")


def alterar(produtos):
    print("\n--- ALTERAR PRODUTO ---")
    try:
        codigo = int(input("Digite o código do produto: "))
    except ValueError:
        print("Digite um número válido.")
        return

    for produto in produtos:
        if produto["id"] == codigo:
            print("Deixe o campo vazio se não quiser alterar.")
            nome = input(f'Nome ({produto["nome"]}): ').strip()
            categoria = input(f'Categoria ({produto["categoria"]}): ').strip()
            descricao = input(f'Descrição ({produto["descricao"]}): ').strip()

            if nome:
                produto["nome"] = nome
            if categoria:
                produto["categoria"] = categoria
            if descricao:
                produto["descricao"] = descricao

            salvar_dados(produtos)
            print("Produto alterado com sucesso!")
            return

    print("Produto não encontrado.")


def excluir(produtos):
    print("\n--- EXCLUIR PRODUTO ---")
    try:
        codigo = int(input("Digite o código do produto: "))
    except ValueError:
        print("Digite um número válido.")
        return

    for produto in produtos:
        if produto["id"] == codigo:
            produtos.remove(produto)
            salvar_dados(produtos)
            print("Produto excluído com sucesso!")
            return

    print("Produto não encontrado.")


def pesquisar(produtos):
    print("\n--- PESQUISAR PRODUTO ---")
    termo = input("Digite o nome, categoria ou descrição: ").strip().lower()

    if termo == "":
        print("Digite algo para pesquisar.")
        return

    encontrados = []
    for produto in produtos:
        if (termo in produto["nome"].lower()
                or termo in produto["categoria"].lower()
                or termo in produto["descricao"].lower()):
            encontrados.append(produto)

    mostrar_produtos(encontrados)


def mostrar_produtos(lista):
    if not lista:
        print("Nenhum produto encontrado.")
        return

    print("\nCódigo | Nome | Categoria | Descrição")
    print("-" * 65)
    for produto in lista:
        print(f'{produto["id"]} | {produto["nome"]} | '
              f'{produto["categoria"]} | {produto["descricao"]}')


def listar_por_nome(produtos):
    print("\n--- PRODUTOS EM ORDEM ALFABÉTICA ---")
    ordenados = sorted(produtos, key=lambda produto: produto["nome"].lower())
    mostrar_produtos(ordenados)


def listar_por_categoria(produtos):
    print("\n--- PRODUTOS POR CATEGORIA ---")
    ordenados = sorted(
        produtos,
        key=lambda produto: produto["categoria"].lower()
    )
    mostrar_produtos(ordenados)


def menu():
    produtos = carregar_dados()

    while True:
        print("\n====== CADASTRO DE PRODUTOS ======")
        print("1 - Incluir produto")
        print("2 - Alterar produto")
        print("3 - Excluir produto")
        print("4 - Pesquisar produto")
        print("5 - Listar por nome")
        print("6 - Listar por categoria")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            incluir(produtos)
        elif opcao == "2":
            alterar(produtos)
        elif opcao == "3":
            excluir(produtos)
        elif opcao == "4":
            pesquisar(produtos)
        elif opcao == "5":
            listar_por_nome(produtos)
        elif opcao == "6":
            listar_por_categoria(produtos)
        elif opcao == "0":
            salvar_dados(produtos)
            print("Dados salvos. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
