from exercicio_polimorfismo.automovel import automovel
from exercicio_polimorfismo.veiculo import veiculo

class moto(automovel):
    def __init__(self, marca, qtd_Rodas, modelo, potenciaMotor ,partidaEletrica, velocidade = 0):
        automovel.__init__(self, marca, qtd_Rodas, modelo, velocidade, potenciaMotor)
        self.partidaEletrica = partidaEletrica

    def imprimirInfos(self):
       print("Marca:", self.marca, "\nRodas: ", self.qtdRodas, "\nModelo:", self.modelo,
             "\nVelocidade:", self.velocidade,"\nPotência do motor : ", self.potenciaMotor, "\nPartida elétrica: " , self.partidaEletrica, )

#partidaEletrica: boolean
#imprimirinfos() : void