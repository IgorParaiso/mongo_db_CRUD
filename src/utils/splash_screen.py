from conexion.mongo_queries import MongoQueries
import pandas as pd
from utils import config

class SplashScreen:

    def __init__(self):
        # Nome(s) do(s) criador(es)
        self.created_by = "ALLAN JONES DA SILVA JESUS\n\t#\tDANIEL MARTINS FERREIRA\n\t#\tIGOR PARAISO DEMUNER\n\t#\tJOSE CARLOS VIEIRA DOS SANTOS JUNIOR\n\t#\tKEVEN DO ROSÁRIO FERREIRA\n\t#\tLUCAS RODRIGUES DA CRUZ"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_count_documents(self, collection_name):
        df = config.query_count(collection_name=collection_name)
        return df[f"total_{collection_name}"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #         SISTEMA DE AGENDAMENTO DE LABORATÓRIOS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - CLIENTES: {str(self.get_count_documents(collection_name="clientes"))}         
        #      2 - LABORATORIOS: {str(self.get_count_documents(collection_name="laboratorios"))}       
        #      3 - AGENDAS: {str(self.get_count_documents(collection_name="agenda"))}    
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """