par = 0
impar = 0
for i in range(10):
    num = int(input("Informe um numero inteiro: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print("Quantidade de numeros pares: ", par)
print("Quantidade de numeros impares: ", impar)
