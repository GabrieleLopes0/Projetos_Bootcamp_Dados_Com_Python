conjunto_vazio = set()
conjunto = {1, 2, 3, 4, 5}
conjunto_strings = {"a", "b", "c"}

print(len(conjunto))
print(2 in conjunto)

conjunto.add(6)
print(conjunto)

conjunto.remove(3)
print(conjunto)

conjunto.discard(10)
print(conjunto)

conjunto2 = {4, 5, 6, 7}
print(conjunto.union(conjunto2))
print(conjunto.intersection(conjunto2))
print(conjunto.difference(conjunto2))
print(conjunto.symmetric_difference(conjunto2))

print(conjunto | conjunto2)
print(conjunto & conjunto2)
print(conjunto - conjunto2)
print(conjunto ^ conjunto2)

for item in conjunto:
    print(item)

conjunto.clear()
print(conjunto)
