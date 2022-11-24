from conexion.mongo_queries import MongoQueries
import pandas as pd

class Relatorio:
    
    def get_relatorio_clientes(self):
        
        mongo = MongoQueries()
        mongo.connect()
        query_results = mongo.db['clientes'].find({})
        df_cliente = pd.DataFrame(list(query_results))
        return df_cliente

    def get_relatorio_laboratorios(self):

        mongo = MongoQueries()
        mongo.connect()

        query_results = mongo.db['laboratorios'].find({})
        df_laboratorio = pd.DataFrame(list(query_results))
        return df_laboratorio
    
    def get_relatorio_agenda(self):

        mongo = MongoQueries()
        mongo.connect()

        query_results = mongo.db['agenda'].find({})
        df_agenda = pd.DataFrame(list(query_results))

        return df_agenda

    def get_relatorio_clientes_lab (self):
        
        mongo = MongoQueries()
        mongo.connect()

        query_results = mongo.db['cliente'].aggregate()

        print(mongo.sqlToDataFrame(self.query_relatorio_clientes_lab))
        input("Pressione Enter para sair do relatório")

    def get_relatorio_total_clientes(self):

        mongo = MongoQueries()
        mongo.connect()

        print(mongo.sqlToDataFrame(self.query_relatorio_total_clientes))
        input("Pressione Enter para sair do relatório")
