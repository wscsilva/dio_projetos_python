import psycopg2

class DB:
    def __init__(self, *, port, database, user, password, host="localhost" ):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cursor = None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(
                database=self.database, 
                port= self.port,
                user=self.user, 
                password=self.password, 
                host=self.host)
            self.cursor = self.conn.cursor()
            print("Conexão estabelecida com sucesso.")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def executar(self, sql, *arqs):
        try:
            self.cursor.execute(sql, arqs)
            self.conn.commit()
        except Exception as e:
            print(f"Erro ao executar {e}")

    def consultar(self, sql):
        self.cursor.execute(sql) 
        return self.cursor.fetchone()
    
    def fechar(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Conexão fechada com sucesso.")
    
    