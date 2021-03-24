class Pessoa:

    def __init__(self, codPessoa , nomePessoa):
        self.codigo = codPessoa
        self.nome = nomePessoa
        self.imprimir()

    def imprimir(self):
        print("Código: " , self.codigo , "\nNome: " , self.nome)