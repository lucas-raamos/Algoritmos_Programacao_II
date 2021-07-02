from Torre import Torre
from Apartamento import Apartamento


blocoA = Torre()
blocoA.cadastrar()
blocoA.imprimir()

blocoB = Torre()
blocoB.cadastrar()
blocoB.imprimir()

ap01 = Apartamento()
ap01.cadastrar(blocoA)
ap01.imprimir()