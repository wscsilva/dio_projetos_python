import datetime

class Transacao:
    saldo = 1000.0
    limite = 300.0
    qtd_saque_dia = 1
    QTD_SAQUE_MAXIMO_DIA = 3
    logs = []

    def depositar(self, valor):
        print(f"Saldo anterior: {self.saldo}")
        self.saldo += valor
        msg = "➕ Depósito realizado com sucesso!"
        self.gravar_log("D", valor, msg)
        print(f'Depósito realizado com sucesso! Saldo atual: {self.saldo}')

    def retirar(self, valor):
        if valor <= self.saldo and valor <= self.limite:
            if self.qtd_saque_dia <= self.QTD_SAQUE_MAXIMO_DIA:
                self.saldo -= valor
                msg = "➖ Saque realizado com sucesso!"
                self.gravar_log("S", valor, msg)
                self.qtd_saque_dia += 1
                print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print(f"⚠️ Você já realizou {self.QTD_SAQUE_MAXIMO_DIA} saques hoje. Por favor, aguarde até o dia seguinte ⚠️")
        else:
            msg = "❌Operação não permitida. Valor excede o saldo ou o limite de saque❌"
            print(msg)

    def gravar_log(self, status, valor, msg):
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        self.logs.append(f"{data_hora} | {msg} |{valor:.2f}| {status}")
        print("Log gravado com sucesso!")
                                                     
    def consultar_log(self):
        print("\n-----------------------------------------------------------------------------")
        print("Movimentações do dia:")
        print("-----------------------------------------------------------------------------")
        logs = self.logs
        if logs:
            for log in self.logs:
                print(log)
        else:
            print("❌ Nenhuma movimentação encontrado!")
        print("-----------------------------------------------------------------------------")
        print(f"Saldo atual: {self.saldo:.2f}")
