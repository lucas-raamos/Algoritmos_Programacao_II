from abc import ABCMeta, abstractmethod

class Computador(metaclass=ABCMeta):

    @abstractmethod
    def get_Informacoes(self, modelo, cor, preco):
        pass

    @abstractmethod
    def cadastrar(self):
        pass