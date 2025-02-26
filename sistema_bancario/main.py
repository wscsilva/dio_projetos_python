# Importando a classe Transacao do arquivo transacao.py
from transacao import Transacao

# Definição da classe principal do sistema bancário
class Main:
    def __init__(self):
        """
        Método construtor da classe Main.
        Executa um loop infinito exibindo um menu interativo para o usuário,
        permitindo operações bancárias como depósito, retirada, consulta de saldo e logs.
        """
        while True:
            self.exibir_menu()

            # Solicita ao usuário que escolha uma opção
            opcao = input("Escolha uma opção: ")

            # Verifica qual opção foi escolhida e executa a ação correspondente
            if opcao == "1":
                # Converte o valor para float e chama o método depositar
                self.depositar() 
            elif opcao == "2":
                # Chama o método retirar
                self.retirar()
            elif opcao == "3":
                # Chama o método consultar_saldo
                self.consultar_saldo()
            elif opcao == "4":
                # Chama o método consultar_log
                self.consultar_log()
            elif opcao == "5":
                # Sai do sistema bancário encerrando o loop
                if input("Tem certeza que deseja sair do sistema? (S/N)").strip().upper() == "S":
                    print("Saindo do sistema!")
                    break
            else:
                # Informa ao usuário que a opção é inválida
                print("❌ Opção inválida. Tente novamente!")

    # Instancia um objeto da classe Transacao para gerenciar transações bancárias
    transacao = Transacao()

    def exibir_menu(self):
        # Exibe o menu de opções
        print("\n### Menu Bancário ###")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Consultar saldo")
        print("4. Consultar log")
        print("5. Sair")

    def depositar(self):
        """
        Método responsável por realizar um depósito na conta bancária.
        Chama o método depositar da classe Transacao.
        :param valor: Valor a ser depositado (float)
        """
        try:
            # Solicita o valor do depósito ao usuário
            valor_deposito = float(input("Digite o valor a ser depositado: ").strip())

            if valor_deposito > 0 :
                self.transacao.depositar(valor_deposito)
                #print(f"✅ Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            else:
                print("❌ O valor do depósito deve ser positivo!")
        except ValueError:
            print("❌ Entrada inválida! Digite um valor numérico.")

    def retirar(self):

        try:
            valor_saque= float(input("Digite o valor a ser sacado: ").strip())

            if valor_saque > 0 :
                self.transacao.retirar(valor_saque)
                #print(f"✅ Saque de R$ {valor_saque:.2f} realizado com sucesso!")
            else:
                print("❌ O valor do saque deve ser positivo!")
        except ValueError:
            print("❌ Entrada inválida! Digite um valor numérico.")


    def consultar_saldo(self):
        """
        Método responsável por consultar o saldo bancário.
        (Ainda não implementado, apenas exibe uma mensagem).
        """
        print("Consultando saldo...")

    def consultar_log(self):
        """
        Método responsável por consultar o log de transações.
        Chama o método consultar_log da classe Transacao.
        """
        self.transacao.consultar_log()

# Verifica se o script está sendo executado diretamente
# Se for o caso, cria e executa a classe Main
if __name__ == "__main__":
    Main()
