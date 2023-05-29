peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))
imc = peso/altura**2

if imc >= 18.5 and imc <= 25.0:
    print("Peso normal!")
elif imc > 25.0:
    print("Acima do peso!")
else:
    print("Abaixo do peso!")
