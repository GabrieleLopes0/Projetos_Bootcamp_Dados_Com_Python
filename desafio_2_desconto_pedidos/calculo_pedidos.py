entrada = input("Digite o valor total do pedido e o percentual de desconto separados por espaço: ")
valor_total, percentual_desconto = entrada.split()
valor_total = float(valor_total)
percentual_desconto = int(percentual_desconto)

desconto = valor_total * (percentual_desconto / 100)
valor_final = valor_total - desconto

print(f"Valor total do pedido: R$ {valor_total:.2f}")
print(f"Percentual de desconto: {percentual_desconto}%")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final do pedido: R$ {valor_final:.2f}")
