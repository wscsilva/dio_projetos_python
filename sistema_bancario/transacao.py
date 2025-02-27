import datetime
from util import Util

class Transacao:
    saldo = 1000.0
    limite = 300.0
    qtd_saque_dia = 1
    QTD_SAQUE_MAXIMO_DIA = 3
    logs = []
    LOG_FILE = "transacoes.log"

    util = Util()

    def depositar(self, valor):
        print(f"Saldo anterior: {self.saldo}")
        self.saldo += valor
        msg = "➕ Depósito realizado com sucesso!"
        self.gravar_log("D", valor, msg)
        print(f'✅ Depósito realizado com sucesso! Saldo atual: {self.util.formatToReal(self.saldo)}')

    def retirar(self, valor):
        if valor <= self.saldo and valor <= self.limite:
            if self.qtd_saque_dia <= self.QTD_SAQUE_MAXIMO_DIA:
                self.saldo -= valor
                msg = "➖ Saque realizado com sucesso!   "
                self.gravar_log("S", valor, msg)
                self.qtd_saque_dia += 1
                print(f"✅ Saque de {self.util.formatToReal(valor)} realizado com sucesso!")
            else:
                print(f"⚠️ Você já realizou {self.QTD_SAQUE_MAXIMO_DIA} saques hoje. Por favor, aguarde até o dia seguinte ⚠️")
        else:
            msg = "❌ Operação não permitida. Valor excede o saldo ou o limite de saque ❌"
            print(msg)

    def gravar_log(self, status, valor, msg):
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        mensagem = f"{data_hora} | {msg} |{valor:.2f}| {status}"
        self.logs.append(mensagem)

        self.gravar_log_arquivo(mensagem)

        print("Log gravado com sucesso!")

    def gravar_log_arquivo(self, mensagem):
        try:
            with open(self.LOG_FILE, "a", encoding="utf-8") as arquivo:
                arquivo.write(mensagem + "\n")
                print("Log gravado com sucesso.")
        except Exception as e:
            print(f"Erro ao gravar log! , {e}")

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
        saldo_final = self.util.formatToReal(self.saldo)
        print(f"💰 Saldo atual: {saldo_final}")
