MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Clientes
2 - Relatório de Agenda
3 - Relatório de Laboratórios
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - CLIENTES
2 - AGENDA
3 - LABORATORIOS
"""

MENU_ATRIBUTOS_CLIENTES = """Atributos de Clientes
- NOME
- TELEFONE
"""

MENU_ATRIBUTOS_AGENDA = """Atributos de Clientes
- DATA
- HORA INICIO
- HORA FIM
"""

MENU_ATRIBUTOS_LABORATORIOS = """Atributos de Clientes
- QUANTIDADE DE MÁQUINAS
- TIPO DE LABORATORIO
"""

# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")