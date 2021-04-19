from exercicio_encapsulamento.pessoa import pessoa
class fisica(pessoa):

    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        pessoa.__init__(self, codigo, nome, endereco, telefone)
        self._cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self._imc = 0

    def _imprimirCpf(self):
        print("CPF: ", self._cpf)

    def calculaIMC(self):
        self._imc = self.peso / (self.altura * self.altura)

    def resultadoIMC(self):
        print("O IMC de %s é %f" % (self.nome, self._imc))

#    def imprimirInfos(self):
 #       print("Codigo: ", self._codigo, "\nNome: ", self.nome, "\nEndereço:", self.__endereco,
  #           "\nTelefone:", self._telefone, "\nCPF: ", self._cpf, "\nIdade: ", self.idade, "\Peso: ", self.peso,
   #          "\nAltura: ", self.altura)

 #   def calculaIMC(self):
  #      imc = peso / (altura * altura)
   #     print('Seu índice de massa corporal é {:.2f}'.format(imc))
