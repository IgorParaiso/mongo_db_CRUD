from model.laboratorios import Laboratorio
from conexion.oracle_queries import OracleQueries

class Controller_Laboratorio:
    def __init__(self):
        pass

    def inserir_laboratorio(self) -> Laboratorio:
        
        # Faz a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        id_lab = int(input('Insira o código do laboratório: '))
        if not self.verifica_se_existe(oracle, id_lab):
            qtd_maquinas = input('Insira a quantidade de máquinas do laboratório: ')
            lab_tipo = input('Insira o tipo de laboratório: ')

            oracle.write(f"insert into laboratorios values ({id_lab},'{qtd_maquinas}', '{lab_tipo}')")

            df_lab = oracle.sqlToDataFrame(f"select id_lab, qtd_maquinas, tipo_lab from laboratorios where id_lab = {id_lab}")

            novo_lab = Laboratorio(df_lab.id_lab.values[0], df_lab.qtd_maquinas.values[0], df_lab.tipo_lab.values[0])

            print(novo_lab.to_string())

            return novo_lab
        else:
            print(f'O código {id_lab} já está cadastrado')
            return None

    def atualizar_laboratorio(self) -> Laboratorio:
        # Faz a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_lab = int(input("Insira o código do laboratorio a ser alterado: "))

        if not self.verifica_se_existe(oracle, id_lab):
            choice = int(input("Escolha uma opção\n1 - Alterar quantidade de máquinas\n2 - Alterar o tipo de laboratório\n"))
            
            if choice == 1:
                nova_qtd_maquinas = input("Digite a nova quantidade de máquinas: ")
                oracle.write(f"update laboratorios set qtd_maquinas = '{nova_qtd_maquinas}' where id_lab = '{id_lab}'")

                df_lab = oracle.sqlToDataFrame(f"select id_lab, qtd_maquinas, tipo_lab from laboratorios where id_lab = '{id_lab}'")
                cliente_atualizado = Laboratorio(df_lab.id_lab.values[0], df_lab.qtd_maquinas.values[0], df_lab.tipo_lab.values[0])
                print(cliente_atualizado.to_string())
                return cliente_atualizado
            
            elif choice == 2:
                novo_tipo_lab = input("Digite o novo tipo_lab: ")
                oracle.write(f"update laboratorios set tipo_lab = '{novo_tipo_lab}' where id_lab = '{id_lab}'")
                df_lab = oracle.sqlToDataFrame(f"select id_lab, qtd_maquinas, tipo_lab from laboratorios where id_lab = '{id_lab}'")
                cliente_atualizado = Laboratorio(df_lab.id_lab.values[0], df_lab.qtd_maquinas.values[0], df_lab.tipo_lab.values[0])
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
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_lab = int(input("Insira o Código do laboratório a ser excluído: "))

        if not self.verifica_se_existe(oracle, id_lab):
            df_cliente = oracle.sqlToDataFrame(f"select id_lab, qtd_maquinas, tipo_lab from laboratorios where id_lab = '{id_lab}'")
            oracle.write(f"delete from laboratorios where id_lab = '{id_lab}'")

            cliente_excluido = Laboratorio(df_cliente.id_lab.values[0], df_cliente.qtd_maquinas.values[0], df_cliente.tipo_lab.values[0])

            print("Cliente Removido com sucesso")
            print(cliente_excluido.to_string())
        
        else:
            print(f"cliente {id_lab} não existe")
            return None

    def verifica_se_existe(self, oracle:OracleQueries, cpf:int=None) -> bool:

        df_cliente = oracle.sqlToDataFrame(f"select id_lab, qtd_maquinas from laboratorios where id_lab = '{cpf}'")
        return df_cliente.empty

