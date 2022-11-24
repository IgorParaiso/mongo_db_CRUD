from model.agenda import Agenda
from conexion.mongo_queries import MongoQueries
from reports.relatorios import Relatorio
import pandas as pd

relatorios = Relatorio()
class Controller_Agenda:
    def __init__(self):
        pass

    def inserir_agenda(self) -> Agenda:
        
        # Faz a conexão com o banco de dados
        mongo = MongoQueries()
        mongo.connect()
        
        print(relatorios.get_relatorio_laboratorios())
        id_lab = int(input('Insira o código do laboratório a ser reservado: '))
        if not self.verifica_se_existe_lab(mongo, id_lab):
            print(relatorios.get_relatorio_clientes())
            cpf = input('Insira o CPF de quem irá reservar o laboratório: ')
            if self.verifica_se_existe_cliente(mongo, cpf):
                
                id_agenda = int(input("Insira o número da reserva: "))
                if self.verifica_se_existe_agenda(mongo, id_agenda):
                    data = input('Insira o dia que o laboratório será reservado (no formato DD/MM/YYYY): ')
                    hora_inicio = input('Insira o horário de início da reserva (no formato HH:MM): ')
                    hora_fim = input('Insira o horário de encerramento da reserva (no formato HH:MM): ')

                    mongo.db["agenda"].insert_one({"cpf":cpf,"id_lab":id_lab,"id_agenda":id_agenda,"data":data,"horainicio":hora_inicio,"horafim":hora_fim})

                    query_result = mongo.db["agenda"].find_one({"cpf":cpf,"id_lab":id_lab,"id_agenda":id_agenda,"data": data,"horainicio":hora_inicio,"horafim":hora_fim})

                    df_agenda = pd.DataFrame(query_result)
                    
                    novo_agenda = Agenda(df_agenda.cpf.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

                    print(novo_agenda.to_string())

                    return novo_agenda
                else:
                    print(f'O número {id_agenda} já existe')
                    return None
            else:
                print(f'O cliente {cpf} não existe')
                return None
        else:
            print(f'O código {id_lab} não existe')
            return None

    def atualizar_agenda(self) -> Agenda:
        
        # Faz a conexão com o banco de dados
        mongo = MongoQueries()
        mongo.connect()
        
        print(relatorios.get_relatorio_agenda())
        id_agenda = int(input('Insira o código de reserva na agenda: '))
        if not self.verifica_se_existe_agenda(mongo, id_agenda):
            choice = int(input("Escolha o atributo a ser  alterado\n1 - Cliente que fez a reserva\n2 - Laboratório que está reservado\n3 - Horário de início\n4 - Horário de Término\n5 - Dia da reserva\n0 - Sair "))

            if choice == 1:
                print(relatorios.get_relatorio_clientes())
                novo_cpf = int(input("Insira o novo CPF do cliente: "))
                if self.verifica_se_existe_cliente(mongo, novo_cpf):
                   print(f'O cliente {novo_cpf} não exite') 
                   return None
                
                mongo.db['agenda'].update_one({'id_agenda':id_agenda}, {'$set': {'cpf':novo_cpf}})

                query_result = mongo.db['agenda'].find({'id_agenda':id_agenda})
                
                df_agenda = pd.DataFrame(list(query_result))

                novo_agenda = Agenda(df_agenda.cpf.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

                print(novo_agenda.to_string())

                return novo_agenda
            elif choice == 2:
                print(relatorios.get_relatorio_laboratorios)
                novo_lab = int(input("Insira o ID do novo laboratorio: "))
                if self.verifica_se_existe_lab(mongo, novo_lab):
                   print(f'O novo laboratório {novo_lab} não exite') 
                   return None
                
                mongo.db['agenda'].update_one({'id_agenda':id_agenda}, {'$set': {'id_lab':novo_lab}})

                query_result = mongo.db['agenda'].find({'id_agenda':id_agenda})
                
                df_agenda = pd.DataFrame(list(query_result))

                novo_agenda = Agenda(df_agenda.cpf.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

                print(novo_agenda.to_string())

                return novo_agenda
            elif choice == 3:
                novo_horario_inicio = input('Insira o novo horário de início: ')
                mongo.db['agenda'].update_one({'id_agenda':id_agenda}, {'$set': {'horainicio':novo_horario_inicio}})
                
                query_result = mongo.db['agenda'].find({'id_agenda':id_agenda})
                
                df_agenda = pd.DataFrame(list(query_result))

                novo_agenda = Agenda(df_agenda.cpf.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

                print(novo_agenda.to_string())

                return novo_agenda
            elif choice == 4:
                novo_horario_fim = input('Insira o novo horário de fim: ')
                mongo.db['agenda'].update_one({'id_agenda':id_agenda}, {'$set': {'horainicio':novo_horario_fim}})
                
                query_result = mongo.db['agenda'].find({'id_agenda':id_agenda})
                
                df_agenda = pd.DataFrame(list(query_result))
                novo_agenda = Agenda(df_agenda.cpf.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

                print(novo_agenda.to_string())

                return novo_agenda
            elif choice == 5:
                nova_data = input('Insira a nova data: ')
                mongo.db['agenda'].update_one({'id_agenda':id_agenda}, {'$set': {'data':nova_data}})
                
                query_result = mongo.db['agenda'].find({'id_agenda':id_agenda})
                
                df_agenda = pd.DataFrame(list(query_result))

                novo_agenda = Agenda(df_agenda.cpf.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

                print(novo_agenda.to_string())

                return novo_agenda
            elif choice == 0:
                print('')
            else:
                print('opção inválida')
                return None

        else:
            print(f'O código {id_agenda} não existe')
            return None
    
    def exclui_agenda(self):
        
        mongo = MongoQueries()
        mongo.connect()

        print(relatorios.get_relatorio_agenda())
        id_agenda = int(input('Escolha a agenda a ser excluida '))

        if self.verifica_se_existe_agenda(mongo, id_agenda):
            print(f'A agenda {id_agenda} não existe')
            return None
        
        confirmation = str(input(f"Tem certeza que quer excluir a agenda {id_agenda}? (Digite S para sim e N para não) "))
        if confirmation.upper() == "S":
            query_result = mongo.db['agenda'].find({'id_agenda':id_agenda})
                
            df_agenda = pd.DataFrame(list(query_result))
            
            mongo.db['agenda'].delete_one({'id_agenda':id_agenda})
            
            agenda_excluida = Agenda(df_agenda.cpf.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

            print("Agenda excluida com sucesso")
            print(agenda_excluida.to_string())
        
        return None


    def verifica_se_existe_lab(self, mongo:MongoQueries, id_lab:int=None) -> bool:
        query_result = mongo.db['laboratorios'].find({'id_lab':id_lab})
        df_lab = pd.DataFrame(list(query_result))
        return df_lab.empty

    def verifica_se_existe_cliente(self, mongo:MongoQueries, cpf:int=None) -> bool:
        query_result = mongo.db['clientes'].find({"cpf":cpf})
        
        df_cliente = pd.DataFrame(list(query_result))
        return df_cliente.empty


    def verifica_se_existe_agenda(self, mongo:MongoQueries, id_agenda:int=None) -> bool:
        query_result = mongo.db['agenda'].find({'id_agenda':id_agenda})
        df_agenda = pd.DataFrame(list(query_result))
        return df_agenda.empty