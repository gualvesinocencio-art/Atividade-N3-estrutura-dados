# Atividade N3 - Estrutura de Dados e Organização de Arquivos

## Cadastro de produtos

Este projeto foi feito em Python e permite cadastrar produtos, alterar e excluir informações, pesquisar registros e mostrar listas em ordens diferentes.

## O que o programa faz

- **Incluir:** cadastra um produto com nome, categoria e descrição.
- **Alterar:** modifica os dados de um produto usando o código.
- **Excluir:** remove um produto pelo código.
- **Pesquisar:** procura uma palavra no nome, na categoria ou na descrição.
- **Listar por nome:** mostra os produtos em ordem alfabética.
- **Listar por categoria:** organiza os produtos pelo nome da categoria.

## Como os dados são salvos

Os registros ficam no arquivo `dados.json`. O programa carrega esse arquivo quando é iniciado e salva as alterações depois das operações. Assim, os dados continuam disponíveis mesmo depois de fechar o programa.

O arquivo `dados.json` é criado automaticamente quando o primeiro produto é cadastrado.

## Como executar

1. Tenha o Python 3 instalado.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:

```bash
python main.py
```

Não é necessário instalar bibliotecas adicionais, pois o programa utiliza recursos que já fazem parte do Python.

## Organização dos arquivos

- `main.py`: contém o código do sistema.
- `dados.json`: é criado automaticamente para armazenar os cadastros.

## Exemplo de cadastro

- Nome: Teclado
- Categoria: Periféricos
- Descrição: Teclado USB

Depois de cadastrar, é possível pesquisar por qualquer uma dessas informações e listar os produtos por nome ou categoria.
