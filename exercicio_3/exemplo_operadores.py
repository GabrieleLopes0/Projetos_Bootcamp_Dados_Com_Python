a = 10
b = 3
c = 5
d = 2
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3)
dicionario = {'chave': 'valor'}

print("Operadores Aritméticos:")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print("Operadores de Comparação:")
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

print("Operadores de Atribuição:")
x = a
print(x)
x += b
print(x)
x -= b
print(x)
x *= b
print(x)
x /= b
print(x)
x //= b
print(x)
x %= b
print(x)
x **= d
print(x)

print("Operadores Lógicos:")
print(a > b and c < d)
print(a > b or c < d)
print(not (a > b))

print("Operadores de Identidade:")
y = a
print(y is a)
print(y is not b)

print("Operadores de Associação:")
print(b in lista)
print(c not in lista)
print(1 in tupla)
print('chave' in dicionario)
