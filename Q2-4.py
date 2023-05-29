valor_saque = float(input("Valor do saque:"))

if valor_saque % 10 == 0 and valor_saque <= 1000:
    print("Preparando saque...")
    notas_200 = valor_saque // 200
    valor_saque = valor_saque % 200

    notas_100 = valor_saque // 100
    valor_saque = valor_saque % 100

    notas_50 = valor_saque // 50
    valor_saque = valor_saque % 50

    notas_10 = valor_saque // 10

    print("Notas de R$200:", notas_200)
    print("Notas de R$100:", notas_100)
    print("Notas de R$50:", notas_50)
    print("Notas de R$10:", notas_10)
else:
    print("Insira um valor valido!")
