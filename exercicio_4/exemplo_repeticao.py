for i in range(5):
    print(i)

lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)

contador = 0
while contador < 5:
    print(contador)
    contador += 1

for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)

soma = 0
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero
print("Soma:", soma)
