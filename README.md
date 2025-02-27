# Sistema Bancário em Python

Este é um projeto de aprendizado desenvolvido em Python que simula um sistema bancário simples. Ele permite realizar operações como depósitos, saques, consultas de saldo e registro de transações em um log estruturado.

## Funcionalidades
- Depósito de valores na conta.
- Retirada de valores da conta.
- Consulta de saldo.
- Registro de transações em log (com data, tipo da transação e valor).
- Consulta do log de transações filtrando por tipo e data.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
/ sistema_bancario
│── main.py          # Arquivo principal que inicia o sistema
│── transacao.py     # Classe para gerenciar transações bancárias
│── db.py            # Classe para interagir com o banco de dados
│── util.py          # Funções utilitárias, como formatação de valores
│── README.md        # Documentação do projeto
```

## Tecnologias Utilizadas
- **Python 3.x**
- **VS Code** como editor de código

## Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone -b sistema_bancario https://github.com/wscsilva/dio_projetos_python.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd sistema_bancario
   ```
3. Execute o sistema:
   ```bash
   python main.py
   ```

## Exemplo de Uso

Ao iniciar o sistema, será exibido um menu interativo onde o usuário pode selecionar opções como:

```
### Menu Bancário ###
1. Depositar
2. Retirar
3. Consultar saldo
4. Consultar log
5. Sair
Escolha uma opção:
```

Se o usuário escolher **1 (Depositar)**, o sistema solicitará o valor do depósito e registrará a transação no log.

## Registro de Transações
As transações são armazenadas em um log no seguinte formato:

```
2025-02-27 | D | 1500.00
2025-02-27 | S | 500.00
```

Onde:
- **D** indica Depósito
- **S** indica Saque
- O primeiro campo é a data da transação
- O último campo é o valor da transação

## Melhorias Futuras
- Implementação de uma interface gráfica (GUI)
- Suporte a múltiplos usuários

---
Desenvolvido para fins educacionais e aprimoramento do conhecimento em Python. ✨

## Contato
📧 **Email:** diasisilva@hotmail.om