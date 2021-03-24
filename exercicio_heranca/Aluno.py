class Aluno:

    def __init__(self, cod_aluno, nome_aluno, matricula_aluno):
        self.codigo = cod_aluno
        self.nome = nome_aluno
        self.matricula = matricula_aluno
        self.imprimir()

    def imprimir(self):
        print("Código: ", self.codigo, "\nNome: ", self.nome, "\nMatricula: ", self.matricula)
