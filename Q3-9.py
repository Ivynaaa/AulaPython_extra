ConceitoA = []  # Notas entre 9.0 e 10.0
ConceitoB = []  # Notas entre 8.0 e 9.0
ConceitoC = []  # Notas entre 7.0 e 8.0
ConceitoD = []  # Notas entre 6.0 e 7.0
ConceitoE = []  # Notas entre 0.0 e 6.0

nota = float(input("Insira as notas de 0 a 10: \n(Para encerrar digite -1)"))
while nota != -1:
    if nota >= 9:
        ConceitoA.append(nota)
    elif nota >= 8:
        ConceitoB.append(nota)
    elif nota >= 7:
        ConceitoC.append(nota)
    elif nota >= 6:
        ConceitoD.append(nota)
    else:
        ConceitoE.append(nota)
    nota = float(
        input("Insira as notas de 0 a 10: \n(Para encerrar digite -1)"))

print("Conceito A:", ConceitoA)
print("Conceito B:", ConceitoB)
print("Conceito C:", ConceitoC)
print("Conceito D:", ConceitoD)
print("Conceito E:", ConceitoE)
