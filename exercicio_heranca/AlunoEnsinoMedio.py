from exercicio_heranca.Aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def __init__(self, cod, name, matricula, ano):
        Aluno.__init__(self, cod, name, matricula)
        self.ano = ano
        print("Ano: ", self.ano)
