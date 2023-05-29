def conta_vogais(string):
    vogal = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for caracter in string.lower():  # lower tranforma em minusculo
        if caracter in vogal:
            count += 1
    return count


string1 = "Alemanha"
print(conta_vogais(string1), "vogais")