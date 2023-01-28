def ImpostoMensal(salario) :
    imposto = 0
    _salario = 0

    if salario > 1903.98:
        # Desconto de 7.50%
        # Operador ternário, se caso 'salario > 2826.65' assinala '922.67', se não, retira a diferença do salário e o valor mínimo da faixa
        # Garantido assim a faixa exata.
        _salario = 922.67 if salario > 2826.65 else salario - 1903.98
        imposto += _salario * 0.075

    if salario > 2826.65 :
        # Desconto de 15.00%
        _salario = 924.40 if salario > 3751.05 else salario - 2826.66
        imposto += _salario * 0.15

    if salario > 3751.05 :
        # Desconto de 22,50%
        _salario = 913.63 if salario > 4664.68 else salario - 3751.06
        imposto += _salario * 0.225

    if salario > 4664.68 :
        # Desconto de 27.50%
        _salario = salario - 4664.68
        imposto += _salario * 0.275

    return imposto

salarios = []
rendaTotal = 0.0
rendaMedia = 0.0
irpfTotal = 0.0
irpfMedio = 0.0
aliquota = 0.0
entrada = ""

while entrada != "s" :
    entrada = input("Digite o seu salário ou 's' para sair: ")

    if entrada != "s" :
        salarios.append(float(entrada))
    
for s in salarios :
    rendaTotal += s
    irpfTotal += ImpostoMensal(s)

irpfMedio = irpfTotal / len(salarios)
rendaMedia = rendaTotal / len(salarios)
aliquota = irpfTotal * 100 / rendaTotal

print("")
print("Renda total:--------R$", round(rendaTotal, 2))
print("Renda média mensal:-R$", round(rendaMedia, 2))
print("IRPF total:---------R$", round(irpfTotal, 2))
print("IRPF médio mensal:--R$", round(irpfMedio, 2))
print("Alíquota efetiva:---R$ " + str(round(aliquota, 2)) + "%")