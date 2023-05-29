def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = float(input("Informe o 1° número:"))
num2 = float(input("Informe o 2° número:"))
print("MDC=", mdc(num1, num2))
