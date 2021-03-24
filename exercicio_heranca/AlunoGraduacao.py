from exercicio_heranca.Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, cod, name, matricula,semestre):
        Aluno.__init__(self, cod, name, matricula)
        self.semestre = semestre
        print("Semestre: ", self.semestre)