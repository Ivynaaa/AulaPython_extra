class Funcionario:
    def __init__(self, name: str, salary: float, sale: int):
        self.name = name
        self.salary = salary
        self.sale = sale

    def receives(self):
        if self.sale >= 50:
            print("Salario + Comissão")
        else:
            print("Sem comissão")
