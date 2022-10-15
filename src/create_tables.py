from conexion.oracle_queries import OracleQueries

def create_tables(query:str):
    list_of_commands = query.split(";")

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:
        if len(command) > 0:
            print(command)
            try:
                oracle.executeDDL(command)
                print("Executado com sucesso")
            except Exception as e:
                print(e)

def run():
    with open("sql/create_tables.sql") as f:
        query_create = f.read()
    print("Criando tabelas...")
    create_tables(query=query_create)
    print("Tabelas criadas com sucesso")

if __name__ == '__main__':
    run()