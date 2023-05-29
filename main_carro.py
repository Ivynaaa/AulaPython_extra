from carro import Carro

meu_carro = Carro(10, 50)  # Consumo de 10 km/l e 50 litros no tanque
meu_carro.andar(200)
print(f"Quantidade de combustível no tanque: {meu_carro.quantidade} litros.")
meu_carro.andar(500)
meu_carro.abastecer(20)
print(f"Quantidade de combustível no tanque: {meu_carro.quantidade} litros.")  