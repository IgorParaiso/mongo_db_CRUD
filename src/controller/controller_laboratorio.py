from model.laboratorios import Laboratorio
from conexion.mongo_queries import MongoQueries
from reports.relatorios import Relatorio
import pandas as pd

relatorio = Relatorio()
class Controller_Laboratorio:
    def __init__(self):
        pass

    def inserir_laboratorio(self) -> Laboratorio:
        
        # Faz a conexão com o banco de dados
        mongo = MongoQueries()
        mongo.connect()
        
        print(relatorio.get_relatorio_laboratorios())
        id_lab = int(input('Insira o código do laboratório: '))
        if self.verifica_se_existe(mongo, id_lab):
            qtd_maquinas = input('Insira a quantidade de máquinas do laboratório: ')
            lab_tipo = input('Insira o tipo de laboratório: ')
            
            mongo.db["laboratorios"].insert_one({"id_lab":id_lab,"qtd_maquinas":qtd_maquinas,"lab_tipo":lab_tipo})

            query_result = mongo.db["laboratorios"].find({"id_lab":id_lab,"qtd_maquinas":qtd_maquinas,"lab_tipo":lab_tipo})
            df_lab = pd.DataFrame(list(query_result))

            novo_lab = Laboratorio(df_lab.id_lab.values[0], df_lab.qtd_maquinas.values[0], df_lab.lab_tipo.values[0])

            print(novo_lab.to_string())

            return novo_lab
        else:
            print(f'O código {id_lab} já está cadastrado')
            return None

    def atualizar_laboratorio(self) -> Laboratorio:
        # Faz a conexão com o banco de dados
        mongo = MongoQueries()
        mongo.connect()

        print(relatorio.get_relatorio_laboratorios())
        id_lab = int(input("Insira o código do laboratorio a ser alterado: "))

        if not self.verifica_se_existe(mongo, id_lab):
            choice = int(input("Escolha uma opção\n1 - Alterar quantidade de máquinas\n2 - Alterar o tipo de laboratório\n"))
            
            if choice == 1:
                nova_qtd_maquinas = input("Digite a nova quantidade de máquinas: ")
                mongo.db['laboratorios'].update_one({'id_lab':id_lab}, {'$set': {'qtd_maquinas':nova_qtd_maquinas}})

                query_result = mongo.db['laboratorios'].find({'id_lab':id_lab})

                df_lab = pd.DataFrame(list(query_result))
                cliente_atualizado = Laboratorio(df_lab.id_lab.values[0], df_lab.qtd_maquinas.values[0], df_lab.lab_tipo.values[0])
                print(cliente_atualizado.to_string())
                return cliente_atualizado
            
            elif choice == 2:
                novo_lab_tipo = input("Digite o novo lab_tipo: ")
                mongo.db['laboratorios'].update_one({'id_lab':id_lab},{'$set':{'lab_tipo':novo_lab_tipo}})
                query_result = mongo.db['laboratorios'].find({'id_lab':id_lab})
                df_lab = pd.DataFrame(list(query_result))
                cliente_atualizado = Laboratorio(df_lab.id_lab.values[0], df_lab.qtd_maquinas.values[0], df_lab.lab_tipo.values[0])
                print(cliente_atualizado.to_string())
                return cliente_atualizado
            
            else:
                print('opção inválida')
                return None
        else:
            print(f"O código de laboratorio {id_lab} não existe.")
            return None
    
    def excluir_laboratorio(self):
        # Faz a conexão com o banco de dados
        mongo = MongoQueries()
        mongo.connect()

        print(relatorio.get_relatorio_laboratorios())
        id_lab = int(input("Insira o Código do laboratório a ser excluído: "))

        if not self.verifica_se_existe(mongo, id_lab):

            if self.verifica_se_existe_agenda(mongo, id_lab):
                
                confirmation = str(input("Tem certeza que quer excluir esse laboratório? (Digite S para sim e N para não) "))
                if confirmation.upper() == "S":
                    query_result = mongo.db['laboratorios'].find({'id_lab':id_lab})
                    df_cliente = pd.DataFrame(list(query_result))
                    mongo.db['laboratorios'].delete_one({'id_lab':id_lab})

                    laboratorio_excluido = Laboratorio(df_cliente.id_lab.values[0], df_cliente.qtd_maquinas.values[0], df_cliente.lab_tipo.values[0])

                    print("Laboratório Removido com sucesso")
                    print(laboratorio_excluido.to_string())
            else:
                confirmation = str(input("O usuário tem registro na tabela agenda, digite S para excluir os registros da tabela agenda e N para voltar ao menu principal: "))
                if confirmation.upper() == "S":
                    query_result = mongo.db['laboratorios'].find({'id_lab':id_lab})
                    df_lab = pd.DataFrame(list(query_result))
                    
                    mongo.db['agendas'].delete_many({'id_lab':id_lab})
                    mongo.db['laboratorios'].delete_one({'id_lab':id_lab})
                    

                    lab_excluido = Laboratorio(df_lab.id_lab.values[0], df_lab.qtd_maquinas.values[0], df_lab.lab_tipo.values[0])

                    print("Laboratorios Removido com sucesso")
                    print(lab_excluido.to_string())
            
        else:
            print(f"Laboratorio {id_lab} não existe")
            return None

    def verifica_se_existe(self, mongo:MongoQueries, id_lab:int=None) -> bool:
        
        query_result = mongo.db['laboratorios'].find({"id_lab":id_lab})
        df_lab = pd.DataFrame(list(query_result))
        
        return df_lab.empty

    def verifica_se_existe_agenda(self, mongo:MongoQueries, id_agenda:int=None) -> bool:
        
        query_result = mongo.db['laboratorios'].find({"id_agenda":id_agenda})
        df_agenda = pd.DataFrame(list(query_result))
        
        return df_agenda.empty