idade = 18
nota = 85
temperatura = 25

if idade >= 18:
    print("Maior de idade")

if nota >= 90:
    print("Nota A")
else:
    print("Nota abaixo de A")

if temperatura > 30:
    print("Quente")
elif temperatura > 20:
    print("Agradável")
else:
    print("Frio")

numero = 10
if numero > 0:
    if numero % 2 == 0:
        print("Número positivo e par")
    else:
        print("Número positivo e ímpar")
else:
    print("Número negativo ou zero")
