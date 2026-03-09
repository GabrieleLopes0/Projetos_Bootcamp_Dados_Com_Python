s = "Olá, mundo!"
print(s.upper())
print(s.lower())
print(s.split(","))
print(s.replace("mundo", "Python"))
print(s.startswith("Olá"))
print(s.endswith("!"))
print(len(s))

nome = "João"
idade = 25
print(f"Meu nome é {nome} e tenho {idade} anos")
print("Meu nome é {} e tenho {} anos".format(nome, idade))
print("Meu nome é %s e tenho %d anos" % (nome, idade))

print(s[0:5])
print(s[6:])
print(s[::-1])
print(s[::2])

texto_multi = """Esta é uma string
com múltiplas linhas.
Pode ter quebras de linha."""
print(texto_multi)

texto_multi2 = '''Outra forma de string
múltipla linhas.'''
print(texto_multi2)
