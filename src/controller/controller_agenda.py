from model.agenda import Agenda
from conexion.oracle_queries import OracleQueries
from reports.relatorios import Relatorio


relatorios = Relatorio()
class Controller_Agenda:
    def __init__(self):
        pass

    def inserir_agenda(self) -> Agenda:
        
        # Faz a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        relatorios.get_relatorio_laboratorios()
        id_lab = int(input('Insira o código do laboratório a ser reservado: '))
        if not self.verifica_se_existe_lab(oracle, id_lab):
            relatorios.get_relatorio_clientes()
            cpf = input('Insira o CPF de quem irá reservar o laboratório: ')
            if not self.verifica_se_existe_cliente(oracle, cpf):
                
                id_agenda = int(input("Insira o número da reserva: "))
                if self.verifica_se_existe_agenda(oracle, id_agenda):
                    data = input('Insira o dia que o laboratório será reservado (no formato DD/MM/YYYY): ')
                    hora_inicio = input('Insira o horário de início da reserva (no formato HH:MM): ')
                    hora_fim = input('Insira o horário de encerramento da reserva (no formato HH:MM): ')

                    oracle.write(f"insert into agenda values ({cpf},{id_lab},{id_agenda}, to_date('{hora_inicio}', 'HH24:MI'), to_date('{hora_fim}', 'HH24:MI'), to_date('{data}', 'DD/MM/YYYY'))")

                    df_agenda = oracle.sqlToDataFrame(f"select id_cliente, id_lab, id_agenda, horaInicio, horaFim, data from agenda where id_agenda = {id_agenda}")

                    novo_agenda = Agenda(df_agenda.id_cliente.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

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
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        relatorios.get_relatorio_laboratorios()
        id_agenda = int(input('Insira o código de reserva do laboratório: '))
        if self.verifica_se_existe_agenda(oracle, id_agenda):
            choice = int(input("Escolha o atributo a ser  alterado\n1 - Cliente que fez a reserva\n2 - Laboratório que está reservado\n3 - Horário de início\n4 - Horário de Término\n5 - Dia da reserva\n0 - Sair "))

            if choice == 1:
                novo_cpf = int(input("Insira o CPF do novo cliente: "))
                if self.verifica_se_existe_cliente(oracle, novo_cpf):
                   print(f'O novo cliente {novo_cpf} não exite') 
                   return None
                
                oracle.write(f"update agenda set id_cliente = {novo_cpf} where id_agenda = {id_agenda}")
                
                df_agenda = oracle.sqlToDataFrame(f"select id_cliente, id_lab, id_agenda, horaInicio, horaFim, data from agenda where id_agenda = {id_agenda}")

                novo_agenda = Agenda(df_agenda.id_cliente.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

                print(novo_agenda.to_string())

                return novo_agenda
            elif choice == 2:
                novo_lab = int(input("Insira o CPF do novo cliente: "))
                if self.verifica_se_existe_lab(oracle, novo_lab):
                   print(f'O novo laboratório {novo_lab} não exite') 
                   return None
                
                oracle.write(f"update agenda set id_lab = {novo_lab} where id_agenda = {id_agenda}")
                
                df_agenda = oracle.sqlToDataFrame(f"select id_cliente, id_lab, id_agenda, horaInicio, horaFim, data from agenda where id_agenda = {id_agenda}")

                novo_agenda = Agenda(df_agenda.id_cliente.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

                print(novo_agenda.to_string())

                return novo_agenda
            elif choice == 3:
                novo_horario_fim = input('Insira o novo horário de início: ')
                oracle.write(f"update agenda set horarioInicio = to_date('{novo_horario_fim}', 'HH24:MI') where id_agenda = {id_agenda}")
                df_agenda = oracle.sqlToDataFrame(f"select id_cliente, id_lab, id_agenda, horaInicio, horaFim, data from agenda where id_agenda = {id_agenda}")

                novo_agenda = Agenda(df_agenda.id_cliente.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

                print(novo_agenda.to_string())

                return novo_agenda
            elif choice == 4:
                novo_horario_fim = input('Insira o novo horário de início: ')
                oracle.write(f"update agenda set horarioFim = to_date('{novo_horario_fim}', 'HH24:MI') where id_agenda = {id_agenda}")
                df_agenda = oracle.sqlToDataFrame(f"select id_cliente, id_lab, id_agenda, horaInicio, horaFim, data from agenda where id_agenda = {id_agenda}")

                novo_agenda = Agenda(df_agenda.id_cliente.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

                print(novo_agenda.to_string())

                return novo_agenda
            elif choice == 5:
                nova_data = input('Insira o novo horário de início: ')
                oracle.write(f"update agenda set data = to_date('{nova_data}', 'DD/MM/YYYY') where id_agenda = {id_agenda}")
                df_agenda = oracle.sqlToDataFrame(f"select id_cliente, id_lab, id_agenda, horaInicio, horaFim, data from agenda where id_agenda = {id_agenda}")

                novo_agenda = Agenda(df_agenda.id_cliente.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

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
        
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        relatorios.get_relatorio_laboratorios()
        id_agenda = int(input('Escolha a agenda a ser excluida '))

        if self.verifica_se_existe_agenda(oracle, id_agenda):
            print(f'A agenda {id_agenda} não existe')
            return None
        
        confirmation = str(input(f"Tem certeza que quer excluir a agenda {id_agenda}? (Digite S para sim e N para não) "))
        if confirmation.upper() == "S":
            df_agenda = oracle.sqlToDataFrame(f"select id_cliente, id_lab, id_agenda, horaInicio, horaFim, data from agenda where id_agenda = {id_agenda}")
            oracle.write(f"delete from agenda where id_agenda = {id_agenda}")
            
            agenda_excluida = Agenda(df_agenda.id_cliente.values[0], df_agenda.id_lab.values[0], df_agenda.id_agenda.values[0], df_agenda.horainicio.values[0], df_agenda.horafim.values[0], df_agenda.data.values[0])

            print("Agenda excluida com sucesso")
            print(agenda_excluida.to_string())
        
        return None


    def verifica_se_existe_lab(self, oracle:OracleQueries, id_lab:int=None) -> bool:

        df_lab = oracle.sqlToDataFrame(f"select id_lab, qtd_maquinas from laboratorios where id_lab = '{id_lab}'")
        return df_lab.empty

    def verifica_se_existe_cliente(self, oracle:OracleQueries, cpf:int=None) -> bool:

        df_cliente = oracle.sqlToDataFrame(f"select id_cliente, nome_cliente from clientes where id_cliente = '{cpf}'")
        return df_cliente.empty

    def verifica_se_existe_agenda(self, oracle:OracleQueries, id_agenda:int=None) -> bool:

        df_agenda = oracle.sqlToDataFrame(f"select id_agenda, id_cliente, id_lab from agenda where id_agenda = '{id_agenda}'")
        return df_agenda.empty