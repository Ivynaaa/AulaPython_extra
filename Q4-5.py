def ocorrencias(string, caracter):
    return string.count(caracter)


string1 = "laranja"
caracter1 = "a"
print("Numero de ocorrencias de:", caracter1, "em ",
      string1, "=", ocorrencias(string1, caracter1))
