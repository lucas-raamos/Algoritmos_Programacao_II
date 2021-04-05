class veiculo():

    def __init__(self, marca,  qtdRodas , modelo, velocidade =0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade


    def imprimirInfos(self):
        print("Marca:", self.marca, "\nRodas: ", self.qtdRodas, "\nModelo:", self.modelo,
             "\nVelocidade:", self.velocidade)


    def acelerar(self, valor):
        self.velocidade += valor
        return self.velocidade

    def frear(self, valor):
        self.velocidade -= valor
        return self.velocidade

 #   def acelerar(self):

 #   def frear(self):

#marca String
#qtdRodas int
#modelo String
#velocidade int = 0
#imprimirinfos() void
#acelerar(valor int) : void
#frear (valor: int) void
