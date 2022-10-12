class Laboratorio:
        def __init__(self, 
                 id_lab:int = None,
                 qtd_maquinas:int = None,
                 tipo_lab:str = None
                ):
            self.set_id_lab(id_lab)
            self.set_qtd_maquinas(qtd_maquinas)
            self.set_tipo_lab(tipo_lab)

        def set_id_lab(self, id_lab:int):
            self.id_lab = id_lab

        def set_qtd_maquinas(self, qtd_maquinas:int):
            self.qtd_maquinas = qtd_maquinas

        def set_tipo_lab(self, tipo_lab:str):
            self.tipo_lab = tipo_lab

        def get_id_lab(self) -> int:
            return self.id_lab

        def get_qtd_maquinas(self) -> int:
            return self.qtd_maquinas

        def get_tipo_lab(self) -> str:
            return self.tipo_lab

        def to_string(self) -> str:
            return f"id_lab: {self.get_id_lab()} | qtd_maquinas: {self.get_qtd_maquinas()} | tipo_lab: {self.get_tipo_lab()}"
