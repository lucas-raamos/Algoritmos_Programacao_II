from Lista import Lista

lista = Lista()
lista.adicionar(43)
lista.adicionar(10)
lista.adicionar(24)
print("Lista ordenada: " + str(lista.tamanho))
lista.printListaOrdenada()
lista.printListaInversa()

valor = input("Digite o valor: ")
lista.adicionar(valor)
print("\n -----------------\n")
lista.printListaOrdenada()
lista.printListaInversa()