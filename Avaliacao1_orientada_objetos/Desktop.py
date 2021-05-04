from Computador import Computador

class Desktop(Computador):
    def cadastrar(self):
        print("Cadastrado com sucesso!!!")


    def get_Informacoes(self, modelo, cor, preco, _potenciaDaFonte):
        print("\n Modelo:", modelo, "\n Cor:", cor, "\n Preço:", preco,
              "\n Fonte:", _potenciaDaFonte)
