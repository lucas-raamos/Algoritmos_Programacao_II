from exercicio_polimorfismo.veiculo import veiculo


class automovel(veiculo):
    def __init__(self, marca, qtd_Rodas, modelo,potenciaMotor, velocidade = 0):
        veiculo.__init__(self, marca, qtd_Rodas, modelo, velocidade)
        self.potenciaMotor = potenciaMotor


    def imprimirInfos(self):
         print("Marca:", self.marca, "\nRodas: ", self.qtdRodas, "\nModelo:", self.modelo,
                 "\nVelocidade:", self.velocidade, "\nPotencia do motor: ", self.potenciaMotor)


#    def imprimirinfos

#potenciaMotor : double
#imprimirinfos(): void
