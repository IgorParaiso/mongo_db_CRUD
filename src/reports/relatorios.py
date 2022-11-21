from conexion.mongo_queries import MongoQueries
import pandas as pd

class Relatorio:

    def __init__(self):
        self.query_relatorio_clientes = f.read()
        
        self.query_relatorio_laboratorios = f.read()

        self.query_relatorio_agenda = f.read()

        self.query_relatorio_clientes_lab = f.read()

        self.query_relatorio_total_clientes = f.read()
    
    def get_relatorio_clientes(self):
        
        mongo = MongoQueries()
        mongo.connect()

        print(pd.read_json(mongo.db["clientes"].find_many({})))
        

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
