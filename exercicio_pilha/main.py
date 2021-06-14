from pilha import Pilha
pilha = Pilha()

pilha.inserir(50)
pilha.inserir(35)
pilha.inserir("Lucas")
pilha.inserir("Testando")
print(pilha)
print("-"*50)
pilha.remover()
print(pilha)
print("-"*35)
pilha.remover()
print(pilha)