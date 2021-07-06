from Autor import Autor

class Livro(Autor):

    def __init__(self, id, titulo, autor):
        self.__id = id
        self.titulo = titulo
        self.autor = autor
