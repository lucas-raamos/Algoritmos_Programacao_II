from Autor import Autor
from Livro import Livro
from Pilha import Pilha

autor1ID = input("Digite o ID do autor 1: ")
autor1NOME = input("Digite o nome do autor 1: ")
autor1 = Autor(autor1ID, autor1NOME)
autor1.imprimir()

print("*----------------------------*")
autor2 = Autor("2", "Lucas")
print("*----------------------------*")
autor3 = Autor("3", "Carlos")
print("*----------------------------*")

autor1.imprimir()
print("*----------------------------*")
autor2.imprimir()
print("*----------------------------*")
autor3.imprimir()
print("*----------------------------*")



livroID = input("Digite o ID do autor 1: ")
livroTitulo = input("Digite o nome do autor 1: ")
livroAutor = autor1.nome_publico
livro = Livro(livroID, livroTitulo, livroAutor)



print(livroID, livroTitulo, livroAutor)


pilha = Pilha()
pilha.empilhar(livro.titulo)
print(pilha)
pilha.remover()
print(pilha)