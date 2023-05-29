def encontra_positivos(lista):
    positivos = [num for num in lista if num >= 0]
    return positivos

lista_int = [5, 8, -2, -4, 8]
print("Positivos:", encontra_positivos(lista_int))