class Torre:
    def __init__(self):
        self.id = int()
        self.nome = str()
        self.endereco = str()

    def cadastrar(self):
        self.id = int(input("Digite o ID da Torre: "))
        self.nome = str(input("Digite o Nome da Torre: "))
        self.endereco = str(input("Digite o Endereço da Torre: "))

    def imprimir(self):
        print(f"Id:  {self.id}  \nNome: {self.nome} \nEndereço: {self.endereco}")