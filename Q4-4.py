def eh_palindromo(string):
    if string == string[::-1]:
        return True
    else:
        return False


string = "arara"
print(eh_palindromo(string))
