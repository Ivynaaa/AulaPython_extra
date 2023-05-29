salario = float(input("Informe o salario:"))
if salario <= 1903.98:
    print("Isento do imposto de renda!")
elif salario <= 2826.65:
    salario = salario*0.075 - 142.80
    print("Valor IMR1: ", salario)
else:
    if salario <= 3751.05:
        salario = salario*0.15 - 354.80
        print("Valor IMR2: ", salario)
    elif salario <= 4664.68:
        salario = salario*0.225 - 636.13
        print("Valor IMR3: ", salario)
    else:
        salario = salario*0.275 - 869.36
        print("Valor IMR4:", salario)
