from conexion.oracle_queries import OracleQueries

class Relatorio:

    def __init__(self):
        with open ("src/sql/relatorio_clientes.sql") as f:
            self.query_relatorio_clientes = f.read()
        
        with open ("src/sql/relatorio_laboratorios.sql") as f:
            self.query_relatorio_laboratorios = f.read()
    
    def get_relatorio_clientes(self):
        
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_clientes))
        input("Pressione Enter para sair do relatório")

    def get_relatorio_laboratorios(self):

        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_laboratorios))
        input("Pressione Enter para sair do relatório")