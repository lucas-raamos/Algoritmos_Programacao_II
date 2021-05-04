from Computador import Computador

class Notebook(Computador):

    def cadastrar(self):
        print("Cadastrado com sucesso!!!")

    def get_Informacoes(self, modelo, cor, preco, __tempoDeBateria):
        print("\n Modelo:", modelo, "\n Cor:", cor, "\n Preço:", preco,
              "\n Bateria:", __tempoDeBateria)

