def potencia(base, expoente):
    resultado = 1
    for i in range(expoente):
        resultado *= base
    return resultado


base = float(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))

resultado = potencia(base, expoente)
print("Potencia de ", base, "sobre", expoente, "= ", resultado)
