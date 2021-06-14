class Node:
    def __init__(self, dado=0, node_anterior=None):
        self.dado = dado
        self.anterior = node_anterior

    def __repr__(self):
        return '%s\n%s' % (self.dado, self.anterior)