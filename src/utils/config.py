MENU_PRINCIPAL = """\tMenu Principal
\t1 - Relatórios
\t2 - Inserir Registros
\t3 - Remover Registros
\t4 - Atualizar Registros
\t5 - Sair"""

MENU_RELATORIOS = """\tRelatórios
\t1 - Relatório de Clientes
\t2 - Relatório de Agenda
\t3 - Relatório de Laboratórios
\t4 - Relatório de laboratórios reservado por clientes
\t5 - Total de reservas feitas por clientes
\t0 - Sair"""

MENU_ENTIDADES = """\tEntidades
\t1 - CLIENTES
\t2 - AGENDA
\t3 - LABORATORIOS
\t0 - SAIR"""

MENU_ATRIBUTOS_CLIENTES = """\tAtributos de Clientes
\t- NOME
\t- TELEFONE"""

MENU_ATRIBUTOS_AGENDA = """\tAtributos de Agenda
\n- DATA
\n- HORA INICIO
\n- HORA FIM
\n- ID CLIENTE
\n- ID LABORATORIO
\n- ID AGENDA"""

MENU_ATRIBUTOS_LABORATORIOS = """\tAtributos de Laboratorio
\t- QUANTIDADE DE MÁQUINAS
\t- TIPO DE LABORATORIO"""

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