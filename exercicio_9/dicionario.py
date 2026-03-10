dicionario_vazio = {}
dicionario = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
dicionario2 = dict(a=1, b=2, c=3)

print(dicionario["nome"])
print(dicionario.get("idade"))
print(dicionario.get("altura", "Não encontrado"))

dicionario["profissao"] = "Engenheiro"
print(dicionario)

print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

for chave in dicionario:
    print(chave, dicionario[chave])

for chave, valor in dicionario.items():
    print(chave, valor)

dicionario.update({"idade": 26, "estado": "SP"})
print(dicionario)

valor_removido = dicionario.pop("cidade")
print(valor_removido)
print(dicionario)

dicionario.clear()
print(dicionario)

print(len(dicionario2))
print("a" in dicionario2)
