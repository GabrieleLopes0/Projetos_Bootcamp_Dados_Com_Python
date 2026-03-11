def saudacao():
    print("Olá, mundo!")

def soma(a, b):
    return a + b

def operacao(a, b, op="+"):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return "Operação inválida"

def soma_variavel(*args):
    return sum(args)

def info_pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

def quadrado(x):
    return x ** 2

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def multiplos_retornos(a, b):
    soma = a + b
    produto = a * b
    return soma, produto

saudacao()
print(soma(3, 5))
print(operacao(10, 5))
print(operacao(10, 5, "-"))
print(soma_variavel(1, 2, 3, 4))
info_pessoa(nome="João", idade=25, cidade="São Paulo")

quadrado_lambda = lambda x: x ** 2
print(quadrado_lambda(4))

print(fatorial(5))

s, p = multiplos_retornos(3, 4)
print(f"Soma: {s}, Produto: {p}")
