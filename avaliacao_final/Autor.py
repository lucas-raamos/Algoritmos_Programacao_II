
class Autor:

    def __init__(self, id, nome_publico):
        self.__id = id
        self.nome_publico = nome_publico
        self.imprimir()

    def imprimir(self):
        print("Id: ", self.__id, "\nNome Publico: ", self.nome_publico)

