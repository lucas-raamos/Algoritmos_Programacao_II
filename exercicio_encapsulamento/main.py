from exercicio_encapsulamento.pessoa import pessoa
from exercicio_encapsulamento.fisica import fisica
from exercicio_encapsulamento.juridica import juridica
print("Pessoa")
pessoa1 = pessoa(1,"Marta", "Av. protásio alves", 32323336)
pessoa1.imprimirNome()
pessoa1._imprimirTel()

print("Pessoa Física")
fisica1 = fisica(2, "luiz", "Av.Oscar Pereira", 32488595, "86760389752", 30 , 68, 1.75)
fisica1._imprimirCpf()
_imc = fisica1
_imc.calculaIMC()
_imc.resultadoIMC()
print("*------Nota fiscal------*")
print("Pessoa Jurídica")
juridica1 = juridica(3, "Farmácia São João", "Av. Castelo Branco", 32336589 ,"14590830000790", "isento", 230)
juridica1._imprimirCnpj()
juridica1.notaFiscal()
#j1.emitirNF()