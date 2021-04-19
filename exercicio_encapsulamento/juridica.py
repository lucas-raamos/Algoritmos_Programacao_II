from exercicio_encapsulamento.pessoa import pessoa
class juridica(pessoa):

    def __init__(self, codigo, nome, endereco, telefone, CNPJ, inscEstadual, qtdFuncionarios):
        pessoa.__init__(self,codigo, nome, endereco, telefone)
        self._cnpj = CNPJ
        self._inscEstadual = inscEstadual
        self.qtdFuncionarios = qtdFuncionarios


    def notaFiscal(self):
        print(self.nome , "\nIncrição Estadual: ", self._inscEstadual)

    def _imprimirCnpj(self):
        print("CNPJ:", self._cnpj)


  #  def emitirNF(self):
