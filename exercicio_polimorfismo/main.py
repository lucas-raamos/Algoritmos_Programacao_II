from exercicio_polimorfismo.veiculo import veiculo
from exercicio_polimorfismo.bicicleta import bicicleta
from exercicio_polimorfismo.automovel import automovel
from exercicio_polimorfismo.moto import moto
from exercicio_polimorfismo.carro import carro
print("*--Veículos--*")
v1 = veiculo("Volksvagem", 4 , "FOX")
v1.imprimirInfos()
print("Velocidade -->> ACELERAR: ", v1.acelerar(100))
print("Velocidade -->> FREAR : ", v1.frear(100))

print("*--Bicicletas--*")
b1 = bicicleta("Caloi", "2", "bmx", 18, 18, 0)
b1.imprimirInfos()
print("Velocidade -->> ACELERAR: ", b1.acelerar(100))
print("Velocidade -->> FREAR : ", b1.frear(100))

print("*--Automóveis--*")
a1 = automovel("Fiat", 4, "Uno", 1.0, 0)
a1.imprimirInfos()
print("Velocidade -->> ACELERAR: ", a1.acelerar(100))
print("Velocidade -->> FREAR : ", a1.frear(100))

print("*--Motos--*")
m1 = moto("Honda", "Twister", 2, 0 , True, 250)
m1.imprimirInfos()
print("Velocidade -->> ACELERAR: ", m1.acelerar(100))
print("Velocidade -->> FREAR : ", m1.frear(100))

print("*--Carros--*")
c1 = carro("Chevrolet", 4, "Corsa", 0 , 4 , 2.0)
c1.imprimirInfos()
print("Velocidade -->> ACELERAR: ", c1.acelerar(100))
print("Velocidade -->> FREAR : ", c1.frear(100))






#auto = automovel()

#m1 = moto()

#c1 = carro()

#pp1 = Perecivel()
#pp2 = Perecivel("Nata")
#pp3 = Perecivel("Costela", 28.99)
#pp4 = Perecivel("Nhoque", 9.98, -15.3)


#b1.imprimirInfos()
#auto.imprimirInfos()
#m1.imprimirInfos()
#c1.imprimirInfos()