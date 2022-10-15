from conexion.oracle_queries import OracleQueries

class Relatorio:

    def __init__(self):
        with open ("src/sql/relatorio_clientes.sql") as f:
            self.query_relatorio_clientes = f.read()
    
    def get_relatorio_clientes(self):
        
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_clientes))
        input("Pressione Enter para sair do relatório")