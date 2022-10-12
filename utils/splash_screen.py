#from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        '''# Consultas de contagem de registros - inicio
        self.qry_total_produtos = config.QUERY_COUNT.format(tabela="produtos")
        self.qry_total_clientes = config.QUERY_COUNT.format(tabela="clientes")
        self.qry_total_fornecedores = config.QUERY_COUNT.format(tabela="fornecedores")
        self.qry_total_pedidos = config.QUERY_COUNT.format(tabela="pedidos")
        self.qry_total_itens_pedido = config.QUERY_COUNT.format(tabela="itens_pedido")
        # Consultas de contagem de registros - fim'''

        # Nome(s) do(s) criador(es)
        self.created_by = "ALLAN JONES DA SILVA JESUS/n DANIEL MARTINS FERREIRA/nIGOR PARAISO DEMUNER/nJOSE CARLOS VIEIRA DOS SANTOS JUNIOR/nKEVEN DO ROSÁRIO FERREIRA/nLUCAS RODRIGUES DA CRUZ"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    '''def get_total_produtos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_produtos)["total_produtos"].values[0]'''

    '''def get_total_clientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_clientes)["total_clientes"].values[0]'''

    '''def get_total_fornecedores(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_fornecedores)["total_fornecedores"].values[0]'''

    '''def get_total_pedidos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_pedidos)["total_pedidos"].values[0]'''

    '''def get_total_itens_pedidos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_itens_pedido)["total_itens_pedido"].values[0]'''

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - PRODUTOS:         
        #      2 - CLIENTES:        
        #      3 - FORNECEDORES:     
        #      4 - PEDIDOS:          
        #      5 - ITENS DE PEDIDOS: 
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """