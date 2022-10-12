from datetime import date
from model.clientes import Cliente
from model.laboratorios import Laboratorio

class Agenda:
    def __init__(self, 
                 horaInicio:int=None,
                 horaFim:float=None,
                 data:date=None,
                 cliente:Cliente=None,
                 laboratorio:Laboratorio=None
                 ):
        self.set_horaInicio(horaInicio)
        self.set_horaFim(horaFim)
        self.set_data(data)
        self.set_cliente(cliente)
        self.set_laboratorio(laboratorio)

    def set_horaInicio(self, horaInicio:int):
        self.horaInicio = horaInicio

    def set_horaFim(self, horaFim:float):
        self.horaFim = horaFim

    def set_data(self, data:date):
        self.data = data
    
    def set_cliente(self, cliente:Cliente):
        self.cliente = cliente

    def set_laboratorio(self, laboratorio:Laboratorio):
        self.laboratorio = laboratorio

    def get_horaInicio(self) -> int:
        return self.horaInicio

    def get_horaFim(self) -> float:
        return self.horaFim

    def get_data(self) -> float:
        return self.data
    
    def get_cliente(self) -> Cliente:
        return self.cliente

    def get_laboratorio(self) -> Laboratorio:
        return self.laboratorio
