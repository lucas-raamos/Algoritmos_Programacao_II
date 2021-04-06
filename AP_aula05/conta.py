class conta:
    #ATENÇÃO --> BOAS PRATICAS

    #2Underlines __ = não pode ser acessado fora desta classe
    # ou seja fortemente privado

    #1Underline _ = não de deve mas ok

    #Sem underline _ = publico

    def __init__(self):
        self.__saldo = 0.0

    def __descontarTarifa(self):
        self.__saldo -= 1.99

    def depositar(self, valor):
        self.__saldo += valor
        self.__descontarTarifa()

    def sacar(self, valor):
        if( self.__saldo - 1.99 >= valor ):
            self.__saldo -= valor
            self.__descontarTarifa()

    def getSaldo(self):
        admin = True
        if admin:
            return self.__saldo

    def setSaldo(self, valor):
        admin = True
        if admin:
            self.__saldo = valor

    def imprimirSaldo(self):
        print("O saldo é: ", self.__saldo)