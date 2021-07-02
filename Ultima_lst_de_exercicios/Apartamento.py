class Apartamento:
    def __init__(self):
        self.id = int()
        self.numero = str()
        self.torre = None
        self.vaga = int()
        self.proximo = None

    def cadastrar(self, valor):
        self.id = int(input("Digite o id do apartamento: "))
        self.numero = str(input("Digite o número do apartamento: "))
        self.torre = valor

    def imprimir(self):
        print(f"Id do Apartamento: {self.id} \nNúmero: {self.numero} \nTorre: {self.torre.nome}")

