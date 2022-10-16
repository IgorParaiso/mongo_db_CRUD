from conexion.oracle_queries import OracleQueries

class Relatorio:

    def __init__(self):
        with open ("src/sql/relatorio_clientes.sql") as f:
            self.query_relatorio_clientes = f.read()
        
        with open ("src/sql/relatorio_laboratorios.sql") as f:
            self.query_relatorio_laboratorios = f.read()

        with open ("src/sql/relatorio_agenda.sql") as f:
            self.query_relatorio_agenda = f.read()

        with open ("src/sql/relatorio_clientes_lab.sql") as f:
            self.query_relatorio_clientes_lab = f.read()

        with open ("src/sql/relatorio_total_clientes.sql") as f:
            self.query_relatorio_total_clientes = f.read()
    
    def get_relatorio_clientes(self):
        
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_clientes))
        

    def get_relatorio_laboratorios(self):

        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_laboratorios))
    
    def get_relatorio_agenda(self):

        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_agenda))

    def get_relatorio_clientes_lab (self):
        
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_clientes_lab))
        input("Pressione Enter para sair do relatório")

    def get_relatorio_total_clientes(self):

        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_total_clientes))
        input("Pressione Enter para sair do relatório")
