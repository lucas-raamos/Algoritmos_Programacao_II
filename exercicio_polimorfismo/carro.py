from exercicio_polimorfismo.automovel import automovel
from exercicio_polimorfismo.veiculo import veiculo

class carro(automovel):
    def __init__(self, marca, qtd_Rodas, modelo, potenciaMotor, qtdPortas, velocidade = 0):
        automovel.__init__(self, marca, qtd_Rodas, modelo, velocidade,potenciaMotor)
        self.qtdPortas = qtdPortas


    def imprimirInfos(self):
      print("Marca:", self.marca, "\nRodas: ", self.qtdRodas, "\nModelo:", self.modelo,
             "\nVelocidade:", self.velocidade, "\nPotencia do motor : ", self.potenciaMotor, "\nPortas: " , self.qtdPortas)

#qtdPortas: int
#imprimirinfos(): void)