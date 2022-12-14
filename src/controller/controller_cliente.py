from model.clientes import Cliente
from conexion.mongo_queries import MongoQueries
from reports.relatorios import Relatorio
import pandas as pd

relatorio = Relatorio()
class Controller_Cliente:
    def __init__(self):
        pass

    def inserir_cliente(self) -> Cliente:
        
        # Faz a conexão com o banco de dados
        mongo = MongoQueries()
        mongo.connect()
        
        print(relatorio.get_relatorio_clientes())
        cpf = input('Insira o cpf do cliente: ')
        if self.verifica_se_existe(mongo, cpf):
            nome = input('Insira o nome do cliente: ')
            telefone = input('Insira o telefone do cliente: ')

            mongo.db["clientes"].insert_one({"cpf":cpf, "nome":nome, "telefone": telefone})
            query_result = mongo.db['clientes'].find({"cpf":cpf})
            df_cliente = pd.DataFrame(list(query_result))
            
            novo_cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0], df_cliente.telefone.values[0])

            print(novo_cliente.to_string())

            return novo_cliente
        else:
            print(f'O CPF {cpf} já está cadastrado')
            return None

    def atualizar_cliente(self) -> Cliente:
        # Faz a conexão com o banco de dados
        mongo = MongoQueries()
        mongo.connect()

        print(relatorio.get_relatorio_clientes())
        cpf = input("Insira o CPF do cliente a ser alterado: ")

        if not self.verifica_se_existe(mongo, cpf):
            choice = int(input("Escolha uma opção\n1 - Alterar nome\n2 - Alterar telefone\n"))
            
            if choice == 1:
                novo_nome = input("Digite o novo nome: ")
                mongo.db['clientes'].update_one({"cpf":cpf}, {"$set": {"nome":novo_nome}})
                query_result = mongo.db["clientes"].find({"cpf":cpf})
                df_cliente = pd.DataFrame(list(query_result))
                cliente_atualizado = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0], df_cliente.telefone.values[0])
                print(cliente_atualizado.to_string())
                return cliente_atualizado
            
            elif choice == 2:
                novo_telefone = input("Digite o novo telefone: ")
                mongo.db['clientes'].update_one({"cpf":cpf}, {"$set": {"telefone":novo_telefone}})
                query_result = mongo.db["clientes"].find({"cpf":cpf})
                df_cliente = pd.DataFrame(list(query_result))
                cliente_atualizado = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0], df_cliente.telefone.values[0])
                print(cliente_atualizado.to_string())
                return cliente_atualizado
            
            else:
                print('opção inválida')
                return None
        else:
            print(f"O cliente {cpf} não existe.")
            return None
    
    def excluir_cliente(self):
        # Faz a conexão com o banco de dados
        mongo = MongoQueries()
        mongo.connect()

        print(relatorio.get_relatorio_clientes())
        cpf = int(input("Insira o CPF do cliente a ser excluído: "))

        if self.verifica_se_existe(mongo, cpf):

            if not self.verifica_se_existe_agenda(mongo, cpf):
                
                confirmation = str(input("Tem certeza que quer excluir esse cliente? (Digite S para sim e N para não) "))
                if confirmation.upper() == "S":
                    query_result = mongo.db["clientes"].find({"cpf":cpf})
                    df_cliente = pd.DataFrame(list(query_result))
                    mongo.db["clientes"].delete_one({"cpf":f"{cpf}"})

                    cliente_excluido = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0], df_cliente.telefone.values[0])

                    print("Cliente Removido com sucesso")
                    print(cliente_excluido.to_string())
            else: 
        
                confirmation = str(input("O usuário tem registro na tabela agenda, digite S para excluir os registros da tabela agenda e N para voltar ao menu principal: "))
                if confirmation.upper() == "S":
                    query_result = mongo.db["clientes"].find({"cpf":cpf})
                    df_cliente = pd.DataFrame(list(query_result))
                    
                    mongo.db["agenda"].delete_many({"cpf":cpf})
                    mongo.db["clientes"].delete_one({"cpf":cpf})

                    cliente_excluido = Cliente(query_result['cpf'], query_result['nome'], query_result['telefone'])

                    print("Cliente Removido com sucesso")
                    print(cliente_excluido.to_string())
        
        else:
            print(f"cliente {cpf} não existe")
            return None

    def verifica_se_existe(self, mongo:MongoQueries, cpf:str=None) -> bool:

        query_result = mongo.db['clientes'].find({"cpf":cpf})
        
        df_cliente = pd.DataFrame(list(query_result))
        return df_cliente.empty

    def verifica_se_existe_agenda(self, mongo:MongoQueries, cpf:str=None) -> bool:
        query_result = mongo.db["agenda"].find({"cpf": cpf})

        df_agenda = pd.DataFrame(list(query_result))
        print(df_agenda)
        return df_agenda.empty
    






    