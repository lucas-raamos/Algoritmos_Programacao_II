class pessoa():
    def __init__(self,codigo, nome, endereco, telefone):
        self._codigo = codigo
        self.nome = nome
        self.__endereco = endereco
        self._telefone = telefone

    def imprimirNome(self):
        print("Nome: ", self.nome)

    def _imprimirTel(self):
        print("Telefone: ", self._telefone)
