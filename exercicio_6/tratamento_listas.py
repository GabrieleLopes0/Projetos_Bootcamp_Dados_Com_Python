lista_vazia = []
lista = [1, 2, 3, 4, 5]
lista_strings = ["a", "b", "c"]

print(lista[0])
print(lista[-1])
print(lista[1:4])
print(len(lista))

lista.append(6)
print(lista)

lista.insert(0, 0)
print(lista)

lista.remove(3)
print(lista)

elemento = lista.pop()
print(elemento)
print(lista)

lista.sort()
print(lista)

lista.reverse()
print(lista)

print(2 in lista)
print(lista.index(4))

lista.extend([7, 8])
print(lista)

lista.clear()
print(lista)
