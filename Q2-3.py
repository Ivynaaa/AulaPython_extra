print("--Escolha o combustivel--")
combustivel = str(input("A-alcool // G-gasolina "))
litro = float(input("Quantos litros:"))

if combustivel == 'A' and litro <= 20:
    litro = litro*2.80-0.03
    print("Alcool1 \nTotal: R$", litro)
elif combustivel == 'A' and litro > 20:
    litro = litro*2.80-0.05
    print("Alcool2 \nTotal: R$", litro)
else:
    if combustivel == 'G' and litro <= 20:
        litro = litro*4.20-0.04
        print("Gasolina1 \nTotal: R$", litro)
    elif combustivel == 'G' and litro > 20:
        litro = litro*4.20-0.06
        print("Gasolina2 \nTotal: R$", litro)
