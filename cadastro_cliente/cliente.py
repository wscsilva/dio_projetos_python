
from db import DB

class Cliente:
    def __init__(self, db):
        self.db = db
    
    def cadastrar_cliente(self, razao_social, bloq="N" ):
        sql = "INSERT INTO wscliente (cli_raz_social, cli_bloq) values(%s, %s)"
        self.db.executar(sql, razao_social, bloq)
        print(f"Cliente {razao_social} cadastrado com sucesso.")

    def listar_cliente(self):
        sql = "SELECT * FROM wscliente limit 1"
        clientes = self.db.consultar(sql)

        for cli_raz_social in clientes:
            print(f"Razão Social: {cli_raz_social}")
    
    def listar_cliente_id(self, cli_codigo):
        sql = "SELECT * FROM wscliente WHERE cli_codigo = %s"
        #sql = "SELECT * FROM wscliente limit 1"
        self.db.consultar(sql, cli_codigo)