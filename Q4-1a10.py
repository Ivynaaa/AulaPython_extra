# //Q1
# def potencia(base, expoente):
#     resultado = 1
#     for i in range(expoente):
#         resultado *= base
#     return resultado


# base = float(input("Informe a base: "))
# expoente = int(input("Informe o expoente: "))

# resultado = potencia(base, expoente)
# print("Potencia de ", base, "sobre", expoente, "= ", resultado)

# //Q2
# def encontra_positivos(lista):
#     positivos = [num for num in lista if num >= 0]
#     return positivos

# lista_int = [5, 8, -2, -4, 8]
# print("Positivos:", encontra_positivos(lista_int))

# //Q3
# def reverso(string):
#     return string[::-1] #-1 percorrer a string de trás para frente.

# string_sem_reverso= "Python"
# print(string_sem_reverso, "-->" ,reverso(string_sem_reverso))

# //Q4
# def eh_palindromo(string):
#     if string == string[::-1]:
#         return True
#     else:
#         return False


# string = "arara"
# print(eh_palindromo(string))


# #//Q5
# def ocorrencias(string, caracter):
#     return string.count(caracter)


# string1 = "laranja"
# caracter1 = "a"
# print("Numero de ocorrencias de:", caracter1, "em ",
#       string1, "=", ocorrencias(string1, caracter1))


# #//Q6
# def tempo_total_segundos(dias, hora, min, seg):
#     segundos = ((dias*24+hora)*60+min)*60+seg
#     return segundos


# dias1 = 2
# hora1 = 5
# min1 = 20
# seg1 = 30
# print("Tempo total:", tempo_total_segundos(
#     dias1, hora1, min1, seg1), "segundos")


# #//Q7
# def conta_vogais(string):
#     vogal = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     for caracter in string.lower():  # lower tranforma em minusculo
#         if caracter in vogal:
#             count += 1
#     return count


# string1 = "Alemanha"
# print(conta_vogais(string1), "vogais")

# #//Q8
# def mdc(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a


# num1 = float(input("Informe o 1° número:"))
# num2 = float(input("Informe o 2° número:"))
# print("MDC=", mdc(num1, num2))


# #//Q9
# class Funcionario:
#     def __init__(self, name: str, salary: float, sale: int):
#         self.name = name
#         self.salary = salary
#         self.sale = sale

#     def receives(self):
#         if self.sale >= 50:
#             print("Salario + Comissão")
#         else:
#             print("Sem comissão")

# ##arq_main
# from funcionario import Funcionario
# f1 = Funcionario('Jão', 1500, 40)
# print(f1.name)
# print(f1.salary)
# print(f1.sale)
# print(f1.receives())

# f2 = Funcionario('Maria', 1500, 55)
# print(f2.name)
# print(f2.salary)
# print(f2.sale)
# print(f2.receives())

# #//Q10
# class Carro:
#     def __init__(self, consumo: float, quantidade: float):
#         self.consumo = consumo
#         self.quantidade = quantidade
#     def andar(self, distancia: float):
#         combustivel_necessario=distancia/self.consumo
#         if combustivel_necessario <= self.quantidade:
#             self.quantidade -= combustivel_necessario
#             print(f"O carro percorreu {distancia} km.")
#         else:
#             print("Combustível insuficiente!")

#     def abastecer(self, quantidadeA: float):
#         self.quantidade += quantidadeA
#         print(f"Abastecidos {quantidadeA} litros de combustível")

# ##arq_main
# from carro import Carro

# meu_carro = Carro(10, 50)  # Consumo de 10 km/l e 50 litros no tanque
# meu_carro.andar(200)
# print(f"Quantidade de combustível no tanque: {meu_carro.quantidade} litros.")
# meu_carro.andar(500)
# meu_carro.abastecer(20)
# print(f"Quantidade de combustível no tanque: {meu_carro.quantidade} litros.")
