class Imposto:
    def __init__(self, salario):
        self.salario = salario

    def calcular_desconto(self):
        if self.salario <= 1100:
            taxa = 0.05
        elif self.salario <= 2500:
            taxa = 0.10
        else:
            taxa = 0.15
        return self.salario * taxa

    def salario_liquido(self):
        desconto = self.calcular_desconto()
        return self.salario - desconto

def calcular_imposto(salario):
    imposto = Imposto(salario)
    desconto = imposto.calcular_desconto()
    liquido = imposto.salario_liquido()
    return desconto, liquido

salario = float(input("Digite o salário: "))
desconto, liquido = calcular_imposto(salario)
print(f"Salário bruto: R$ {salario:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Salário líquido: R$ {liquido:.2f}")
