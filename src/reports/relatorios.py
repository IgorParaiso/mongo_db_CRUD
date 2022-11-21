from conexion.mongo_queries import MongoQueries
import pandas as pd

class Relatorio:

    def __init__(self):
        self.query_relatorio_clientes = ""
        
        self.query_relatorio_laboratorios = ""

        self.query_relatorio_agenda = ""

        self.query_relatorio_clientes_lab = ""

        self.query_relatorio_total_clientes = ""
    
    def get_relatorio_clientes(self):
        
        mongo = MongoQueries()
        mongo.connect()
        query_results = mongo.db['clientes'].find({})
        df_cliente = pd.DataFrame(list(query_results))
        print(df_cliente)
        
        

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
