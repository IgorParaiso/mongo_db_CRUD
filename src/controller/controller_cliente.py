from model.clientes import Cliente
from conexion.oracle_queries import OracleQueries

class Controller_Cliente:
    def __init__(self):
        pass

    def inserir_cliente(self) -> Cliente:
        
        # Faz a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        nome = input('Insira o nome do cliente: ')
        telefone = input('Insira o telefone do cliente')

        oracle.write(f"insert into clientes values ('{nome}', '{telefone}')")

        df_cliente = oracle.sqlToDataFrame(f"select nome, telefone from clientes where nome = '{nome}' and telefone = '{telefone}'")

        novo_cliente = Cliente(df_cliente.nome.values[0], df_cliente.telefone.values[0])

        print(novo_cliente.to_string())

        return novo_cliente

    def atualizar_cliente(self) -> Cliente:
        # Faz a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        nome = input("Insira o nome do cliente a ser alterado: ")

        if not self.verifica_se_existe(oracle, nome):
            choice = input("Escolha uma opção\n1 - Alterar nome\n2 - Alterar telefone")
            
            if choice == 1:
                novo_nome = input("Digite o novo nome: ")
                oracle.write(f"update clientes set nome = '{novo_nome}' where nome = '{nome}")

                df_cliente = oracle.sqlToDataFrame(f"select nome, telefone from clientes where nome = '{nome}'")
                cliente_atualizado = Cliente(df_cliente.nome.values[0], df_cliente.telefone.values[0])
                print(cliente_atualizado.to_string())
                return cliente_atualizado
            
            elif choice == 2:
                novo_telefone = input("Digite o novo telefone: ")
                oracle.write(f"update clientes set telefone = '{novo_telefone}' where nome = '{nome}")
                df_cliente = oracle.sqlToDataFrame(f"select nome, telefone from clientes where nome = '{nome}'")
                cliente_atualizado = Cliente(df_cliente.nome.values[0], df_cliente.telefone.values[0])
                print(cliente_atualizado.to_string())
                return cliente_atualizado
            
            else:
                print('opção inválida')
                return None
        else:
            print(f"O cliente {nome} não existe.")
            return None
    
    def excluir_cliente(self):
        # Faz a conexão com o banco de dados
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        nome = input("Insira o nome do cliente a ser excluído: ")

        if self.verifica_se_existe(oracle, nome):
            df_cliente = oracle.sqlToDataFrame(f"select nome, telefone from clientes where nome = '{nome}'")
            oracle.write(f"delete from clientes where nome = '{nome}'")

            cliente_excluido = Cliente(df_cliente.nome.values[0], df_cliente.telefone.values[0])

            print("Cliente Removido com sucesso")
            print(cliente_excluido.to_string())
        
        else:
            print("cliente {nome} não existe")
            return None

    def verifica_se_existe(self, oracle:OracleQueries, nome:str=None) -> bool:

        df_cliente = oracle.sqlToDataFrame(f"select nome, telefone from clientes where nome = '{nome}'")
        return df_cliente.empty