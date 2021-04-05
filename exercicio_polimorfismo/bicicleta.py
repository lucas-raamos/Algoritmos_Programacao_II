from exercicio_polimorfismo.veiculo import veiculo

class bicicleta(veiculo):
    numMarchas: int
    bagageiro: bool

    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro, velocidade = 0):
        veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro


    def imprimirInfos(self):
        print("Marca: " , self.marca, "\nRodas : ", self.qtdRodas, "\nModelo: ", self.modelo,
             "\nVelocidade: ",  self.velocidade, "\nNúmero de marchas: " , self.numMarchas, "\nBagageiro: ", self.bagageiro)

#    def imprimir(self):

#numMarchas: int
#bagageiro : boolean
#imprimirinfors() : void
