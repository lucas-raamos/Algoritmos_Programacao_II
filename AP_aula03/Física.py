from AP_aula03.Pessoa import Pessoa

class Física(Pessoa):

    def __init__(self, cod, name, cpf):
        Pessoa.__init__(self, cod, name)
        self.cpf = cpf
        print("CPF: " , self.cpf)

