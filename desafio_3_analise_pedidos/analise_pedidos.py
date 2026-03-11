entrada = input("Digite o valor do pedido e a prioridade separados por espaço: ").split()
valor = int(entrada[0])
prioridade = entrada[1]

print(f"Valor do pedido: {valor}")
print(f"Prioridade: {prioridade}")

if prioridade == "baixa":
    decisao = "rejeitado"
elif prioridade == "alta":
    if valor <= 1000:
        decisao = "aprovado"
    else:
        decisao = "revisao"
elif prioridade == "media":
    decisao = "aprovado"
else:
    decisao = "rejeitado"

print(f"Decisão: {decisao}")
