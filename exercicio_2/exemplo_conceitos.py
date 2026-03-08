
inteiro = 10  
flutuante = 3.14 
texto = "Olá, mundo!" 
booleano = True  
lista = [1, 2, 3] 

print("Tipos de dados:")
print(f"Inteiro: {inteiro} (tipo: {type(inteiro)})")
print(f"Flutuante: {flutuante} (tipo: {type(flutuante)})")
print(f"Texto: {texto} (tipo: {type(texto)})")
print(f"Booleano: {booleano} (tipo: {type(booleano)})")
print(f"Lista: {lista} (tipo: {type(lista)})")


variavel = "valor inicial"
print(f"\nVariável: {variavel}")
variavel = "valor alterado"
print(f"Variável alterada: {variavel}")

CONSTANTE = 42
print(f"Constante: {CONSTANTE}")

numero_str = "123"
numero_int = int(numero_str)  
numero_float = float(numero_str)  
texto_int = str(inteiro)  

print("\nConversão de tipos:")
print(f"String '123' para int: {numero_int} (tipo: {type(numero_int)})")
print(f"String '123' para float: {numero_float} (tipo: {type(numero_float)})")
print(f"Int 10 para string: {texto_int} (tipo: {type(texto_int)})")

print("\nFunções de entrada:")
nome = input("Digite seu nome: ")
idade_str = input("Digite sua idade: ")
idade = int(idade_str)  

print(f"Olá, {nome}! Você tem {idade} anos.")