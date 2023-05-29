class Carro:
    def __init__(self, consumo: float, quantidade: float):
        self.consumo = consumo
        self.quantidade = quantidade
    def andar(self, distancia: float):
        combustivel_necessario=distancia/self.consumo
        if combustivel_necessario <= self.quantidade:
            self.quantidade -= combustivel_necessario
            print(f"O carro percorreu {distancia} km.")
        else:
            print("Combustível insuficiente!")
    
    def abastecer(self, quantidadeA: float):
        self.quantidade += quantidadeA
        print(f"Abastecidos {quantidadeA} litros de combustível")
