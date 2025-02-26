class Motor:
    def __init__(self, tipo, ano):
        self.tipo = tipo
        self.ano = ano

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor("V8", 2000)  # O carro sempre tem um motor

meu_carro = Carro("Mustang")
print(f"Carro - {meu_carro.motor.tipo} | Modelo - {meu_carro.modelo} | Ano - {meu_carro.motor.ano}")  # Saída: V8
print(meu_carro.modelo)
print(meu_carro.motor.ano)