hora = float(input("Quanto voce ganha por hora trabalhada: "))
trab = float(input("Trabalhou quantas horas no mes: "))
bruto = hora*trab
ir = bruto*0.15
inss = bruto*0.10
sindicato = bruto*0.02
salario_liquido = bruto-ir-inss-sindicato
print("Salario bruto:R$", bruto)
print("INSS:R$", inss)
print("Sindicato:R$", sindicato)
print("Salario liquido:R$", salario_liquido)
