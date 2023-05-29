numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print(numero, "não é primo")
else:
    eh_primo = True
    divisores = []
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            divisores.append(i)

    if eh_primo:
        print(numero, "é primo.")
    else:
        print(numero, "não é primo. É divisível por:", divisores)
