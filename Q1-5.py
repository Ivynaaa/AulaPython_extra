import math

print("---BEM VINDO A TINTA & CIA---")
area=float(input("Informe o da area a ser pintado em metros quadrado:"))
litro= math.ceil( area/3) #funcao de arredondamento
latas=math.ceil(litro/18)
preco= latas*80

print("Latas necessarias: ",latas)
print("Valor total:R$", preco)
