#Construir um algoritmo que contenha 3 listas:
#•  Nomes de produtos
#•  Preços de cada produto
#•  Quantidades de cada produto
#Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas


nome_produtos = []
preco_produtos = []
qtd_produtos = []

def nomes_produtos():
    while True:
        nome_produto = input("Digite o nome do produto: ")
        if nome_produto not in nome_produtos:
            nome_produtos.append(nome_produto)
        else:
            input("Produto ja cadastrado")
        precos_produtos()
        menu()


def precos_produtos():
    while True:
        preco_produto = input("Digite o preço do produto: ")
        if preco_produto not in preco_produtos:
            preco_produtos.append(preco_produto)
        qtds_produtos()


def qtds_produtos():
    while True:
        qtd_produto = input("Digite a quantidade: ")
        if qtd_produto not in preco_produtos:
            preco_produtos.append(qtd_produto)
        input("Produto cadastrado!!! [ENTER] ")
        menu()



def fim_programa():
    while True:
        fim_menu = input("Deseja encerrar o programa? S/N?").lower()
        if fim_menu not in "sn" or fim_menu == "":
            input("Escolha apenas s ou n, por favor [ENTER]")
            continue
        if fim_menu == "s":
            print("Fim do programa!")
            exit()
        else: break

def imprimir_produtoescolhido():
    print(nome_produtos)
    produto_escolhido = input("Digite um produto: ")
    for ind, produto in enumerate(nome_produtos):
        if produto == produto_escolhido:
            print("\t-", nome_produtos[ind])
        input("[ENTER]")

def excluir_por_nomeproduto():
    print("Excluir produto")
    print(nome_produtos)
    produto_a_excluir = input("Digite o produto a ser excluído: ")
    for ind, produto in enumerate(nome_produtos):
        if produto == produto_a_excluir:
            nome_produtos.pop(ind)
    input("Exclusão realizada. [ENTER]")

def menu():
    while True:
        escolha = input('''
        Menu
        0 - Finalizar o Programa
        1 - Cadastrar produtos
        2 - Imprimir um produto
        3 - Excluir um produto
        Escolha: ''')

        if escolha == "0": fim_programa()
        elif escolha == "1": nomes_produtos()
        elif escolha == "2": imprimir_produtoescolhido()
        elif escolha == "3": excluir_por_nomeproduto()
        else: input("Opção inválida [ENTER]")
menu()