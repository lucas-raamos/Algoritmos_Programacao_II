from node import Node


class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def inserir(self, novo_dado):
        novo_node = Node(novo_dado)
        novo_node.anterior = self.topo
        self.topo = novo_node
        self.tamanho = self.tamanho + 1

    def remover(self):
        assert self.topo, "Impossível remover valor de Pilha vazia"
        self.topo = self.topo.anterior
        self.tamanho = self.tamanho - 1

    def __repr__(self):
        return str(self.topo) + '->Tamanho da pilha: ' + str(self.tamanho)

