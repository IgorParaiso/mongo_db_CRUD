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
        pipeline = [
            { '$lookup': {
            'from': 'clientes',
            'localField': 'cpf',
            'foreignField': 'cpf',
            'as': 'users'
            }},
            {"$unwind": { "path": "$users"}},
            {
            '$lookup': {
            'from': 'laboratorios',
            'localField': 'id_lab',
            'foreignField': 'id_lab',
            'as': 'laboratorios'
            }
            },
            { "$unwind": {"path": "$laboratorios"}},
            { "$project": {
            "Nome_Cliente": "$users.nome",
            "data":1,
            "Tipo_Laboratorio": "$laboratorios.lab_tipo",
            "_id":0
            }}
        ]
        query_results = mongo.db['agenda'].aggregate(pipeline)
        df_relatorio = pd.DataFrame(list(query_results))
        print(df_relatorio)
        input("Pressione Enter para sair do relatório")

    def get_relatorio_total_clientes(self):

        mongo = MongoQueries()
        mongo.connect()

        pipeline = [
            {
            '$group': {
                '_id': '$cpf',
                'qtd_reservas': {
                    '$sum':1
                }
            }},
            { '$lookup': {
            'from':"clientes",
            'localField': '_id',
            'foreignField':'cpf',
            'as':'users'
            }},
            {
            '$unwind': {
            'path':'$users'
            }
            },            
            { '$project': {
            "_id":1,
            "cpf":1,
            "nome":"$users.nome",
            "qtd_reservas":1
            }}

        ]
        query_results = mongo.db['agenda'].aggregate(pipeline)
        df_relatorio = pd.DataFrame(list(query_results))
        print(df_relatorio)
        input("Pressione Enter para sair do relatório")
