from db import DB
from cliente import Cliente

banco = DB(port="5433", database="zico", user="postgres", password="Maker@1" )
banco.conectar()

cliente = Cliente(banco)

#cliente.cadastrar_cliente("wilson Carlos da Silva")
cliente.listar_cliente()