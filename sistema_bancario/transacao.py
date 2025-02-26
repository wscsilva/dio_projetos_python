
class Transacao:
    saldo = 1000.0
    limit = 300.0
    qtd_saque_dia = 3
    logs = []

    def depositar(self, valor):
        print(f"Saldo anterior: {self.saldo}")
        self.saldo += valor
        self.gravar_log(valor)
        print(f'Depósito realizado com sucesso! Saldo atual: {self.saldo}')

    def gravar_log(self, valor):
        # Gravar a data
        # Separar por tipo ex: D deposito, S saque
        self.logs.append(f"Deposito efetuado com sucesso, no valor de: R$ {valor:.2f}")
        print("Log gravado com sucesso!")

    def consultar_log(self):
        for log in self.logs:
            print(log)
