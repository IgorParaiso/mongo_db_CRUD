from model.clientes import Cliente
from conexion.oracle_queries import OracleQueries
from reports.relatorios import Relatorio

relatorio = Relatorio()
class Controller_Cliente:
    def __init__(self):
        pass

    def inserir_cliente(self) -> Cliente:
        
        # Faz a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        print(relatorio.get_relatorio_clientes())
        cpf = int(input('Insira o cpf do cliente: '))
        if self.verifica_se_existe(oracle, cpf):
            nome = input('Insira o nome do cliente: ')
            telefone = input('Insira o telefone do cliente: ')

            oracle.write(f"insert into clientes values ({cpf},'{nome}', '{telefone}')")

            df_cliente = oracle.sqlToDataFrame(f"select id_cliente, nome_cliente, telefone from clientes where id_cliente = {cpf}")

            novo_cliente = Cliente(df_cliente.id_cliente.values[0], df_cliente.nome_cliente.values[0], df_cliente.telefone.values[0])

            print(novo_cliente.to_string())

            return novo_cliente
        else:
            print(f'O CPF {cpf} já está cadastrado')
            return None

    def atualizar_cliente(self) -> Cliente:
        # Faz a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        print(relatorio.get_relatorio_clientes())
        cpf = int(input("Insira o CPF do cliente a ser alterado: "))

        if not self.verifica_se_existe(oracle, cpf):
            choice = int(input("Escolha uma opção\n1 - Alterar nome\n2 - Alterar telefone\n"))
            
            if choice == 1:
                novo_nome = input("Digite o novo nome: ")
                oracle.write(f"update clientes set nome_cliente = '{novo_nome}' where id_cliente = '{cpf}'")

                df_cliente = oracle.sqlToDataFrame(f"select id_cliente, nome_cliente, telefone from clientes where id_cliente = '{cpf}'")
                cliente_atualizado = Cliente(df_cliente.id_cliente.values[0], df_cliente.nome_cliente.values[0], df_cliente.telefone.values[0])
                print(cliente_atualizado.to_string())
                return cliente_atualizado
            
            elif choice == 2:
                novo_telefone = input("Digite o novo telefone: ")
                oracle.write(f"update clientes set telefone = '{novo_telefone}' where id_cliente = '{cpf}'")
                df_cliente = oracle.sqlToDataFrame(f"select id_cliente, nome_cliente, telefone from clientes where id_cliente = '{cpf}'")
                cliente_atualizado = Cliente(df_cliente.id_cliente.values[0], df_cliente.nome_cliente.values[0], df_cliente.telefone.values[0])
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
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        print(relatorio.get_relatorio_clientes())
        cpf = int(input("Insira o CPF do cliente a ser excluído: "))

        if not self.verifica_se_existe(oracle, cpf):

            if self.verifica_se_existe_agenda(oracle, cpf):
                
                confirmation = str(input("Tem certeza que quer excluir esse cleinte? (Digite S para sim e N para não) "))
                if confirmation.upper() == "S":
                    df_cliente = oracle.sqlToDataFrame(f"select id_cliente, nome_cliente, telefone from clientes where id_cliente = '{cpf}'")
                    oracle.write(f"delete from clientes where id_cliente = '{cpf}'")

                    cliente_excluido = Cliente(df_cliente.id_cliente.values[0], df_cliente.nome_cliente.values[0], df_cliente.telefone.values[0])

                    print("Cliente Removido com sucesso")
                    print(cliente_excluido.to_string())
            
            confirmation = str(input("O usuário tem registro na tabela agenda, digite S para excluir os registros da tabela agenda e N para voltar ao menu principal: "))
            if confirmation.upper() == "S":
                df_cliente = oracle.sqlToDataFrame(f"select id_cliente, nome_cliente, telefone from clientes where id_cliente = '{cpf}'")
                oracle.write(f"delete from agenda where id_cliente = '{cpf}'")
                oracle.write(f"delete from clientes where id_cliente = '{cpf}'")

                cliente_excluido = Cliente(df_cliente.id_cliente.values[0], df_cliente.nome_cliente.values[0], df_cliente.telefone.values[0])

                print("Cliente Removido com sucesso")
                print(cliente_excluido.to_string())
        
        else:
            print(f"cliente {cpf} não existe")
            return None

    def verifica_se_existe(self, oracle:OracleQueries, cpf:int=None) -> bool:

        df_cliente = oracle.sqlToDataFrame(f"select id_cliente, nome_cliente from clientes where id_cliente = '{cpf}'")
        return df_cliente.empty

    def verifica_se_existe_agenda(self, oracle:OracleQueries, id_agenda:int=None) -> bool:

        df_agenda = oracle.sqlToDataFrame(f"select id_agenda, id_cliente, id_lab from agenda where id_cliente = '{id_agenda}'")
        return df_agenda.empty