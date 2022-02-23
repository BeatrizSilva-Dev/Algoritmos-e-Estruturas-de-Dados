from src.Lista import Lista

lista = Lista()
lista.add_fim(10)
lista.add_fim(20)
lista.add_fim(30)
lista.add_fim(40)

print(lista)
lista.remover_inicio()
print(lista)

lista.remover_fim()
print(lista)
print(len(lista))
