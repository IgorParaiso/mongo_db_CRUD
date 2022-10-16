from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_clientes = config.QUERY_COUNT.format(tabela="clientes")
        self.qry_total_laboratorios = config.QUERY_COUNT.format(tabela="laboratorios")
        self.qry_total_agenda = config.QUERY_COUNT.format(tabela="agenda")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "ALLAN JONES DA SILVA JESUS\n\t#\tDANIEL MARTINS FERREIRA\n\t#\tIGOR PARAISO DEMUNER\n\t#\tJOSE CARLOS VIEIRA DOS SANTOS JUNIOR\n\t#\tKEVEN DO ROSÁRIO FERREIRA\n\t#\tLUCAS RODRIGUES DA CRUZ"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_total_clientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_clientes)["total_clientes"].values[0]

    def get_total_laboratorios(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_laboratorios)["total_laboratorios"].values[0]

    def get_total_agenda(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_agenda)["total_agenda"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #         SISTEMA DE AGENDAMENTO DE LABORATÓRIOS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - CLIENTES: {str(self.get_total_clientes())}         
        #      2 - LABORATORIOS: {str(self.get_total_laboratorios())}       
        #      3 - AGENDAS: {str(self.get_total_agenda())}    
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """