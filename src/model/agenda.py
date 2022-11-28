from datetime import *


class Agenda:
    def __init__(self, 
                 cpf:str=None,
                 laboratorio:int=None,
                 id_agenda:int=None,
                 horaInicio:datetime =None, 
                 horaFim:datetime =None, 
                 data:date=None  
                 ):
        self.set_horaInicio(horaInicio)
        self.set_horaFim(horaFim)
        self.set_data(data)
        self.set_cpf(cpf)
        self.set_laboratorio(laboratorio)
        self.set_id_agenda(id_agenda)

    def set_horaInicio(self, horaInicio:datetime): 
        self.horaInicio = horaInicio

    def set_horaFim(self, horaFim:datetime): #datetime
        self.horaFim = horaFim

    def set_data(self, data:date): #date
        self.data = data
    
    def set_cpf(self, cpf:str):
        self.cpf = cpf

    def set_laboratorio(self, laboratorio:int):
        self.laboratorio = laboratorio
    
    def set_id_agenda(self, id_agenda:int):
        self.id_agenda = id_agenda

    def get_horaInicio(self) -> time: #time
        return self.horaInicio

    def get_horaFim(self) -> time:  #time
        return self.horaFim

    def get_data(self) -> date:  #date
        return self.data
    
    def get_cpf(self) -> str:
        return self.cpf

    def get_laboratorio(self) -> int:
        return self.laboratorio
    
    def get_id_agenda(self) -> int:
        return self.id_agenda

    def to_string(self) -> str:
        return f"cpf: {self.get_cpf()} | Laboratório: {self.get_laboratorio()}\nHorario: {self.get_data()} - {self.get_horaInicio()}"
