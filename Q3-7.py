n = int(input("Digite o tamanho do quadrado: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print(i, "* " * n)
    else:
        print(i, "* " + "  " * (n - 2) + "*")
