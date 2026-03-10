tupla_vazia = ()
tupla = (1, 2, 3, 4, 5)
tupla_strings = ("a", "b", "c")

print(tupla[0])
print(tupla[-1])
print(tupla[1:4])
print(len(tupla))

print(tupla.count(2))
print(tupla.index(4))

a, b, c = tupla_strings
print(a)
print(b)
print(c)

tupla_unica = (5,)
print(tupla_unica)

tupla_concat = tupla + (6, 7)
print(tupla_concat)

print(3 in tupla)
print(max(tupla))
print(min(tupla))
