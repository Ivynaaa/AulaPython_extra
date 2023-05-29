while True:
    nome = input("Digite o nome: ")
    if len(nome) > 3:
        break

while True:
    idade = int(input("Digite a idade: "))
    if 0 <= idade <= 150:
        break

while True:
    salario = float(input("Digite o salário: "))
    if salario > 0:
        break

while True:
    sexo = input("Digite o sexo 'F' ou 'M': ")
    if sexo == 'F' or sexo == 'M':
        break

while True:
    estado_civil = input("Digite o estado civil 'S', 'C', 'V', 'D': ")
    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':
        break
print("Informações válidas:")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)


# maneira alternativa com dicionario
# validacoes = {
#     'Nome': lambda x: len(x) > 3,
#     'Idade': lambda x: 0 <= int(x) <= 150,
#     'Salário': lambda x: float(x) > 0,
#     'Sexo': lambda x: x in ['F', 'M'],
#     'Estado Civil': lambda x: x in ['S', 'C', 'V', 'D']
# }

# informacoes = {}

# for campo, validacao in validacoes.items():
#     while True:
#         valor = input(f"Digite o {campo}: ")
#         if validacao(valor):
#             informacoes[campo] = valor
#             break

# print("Informações válidas:")
# for campo, valor in informacoes.items():
#     print(campo + ":", valor)
