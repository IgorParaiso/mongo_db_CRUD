class Cliente:
    def __init__(self,
                 id_cliente:int=None,
                 nome_cliente:str=None,
                 telefone:str=None):
        self.set_id_cliente(id_cliente)
        self.set_nome_cliente(nome_cliente)
        self.set_telefone(telefone)

    def set_id_cliente(self, id_cliente:int):
        self.id_cliente = id_cliente

    def set_nome_cliente(self, nome_cliente:str):
        self.nome_cliente = nome_cliente

    def set_telefone(self, telefone:int):
        self.telefone = telefone

    def get_id_cliente(self) -> int:
        return self.id_cliente

    def get_nome_cliente(self) -> str:
        return self.nome_cliente

    def get_telefone(self) -> str:
        return self.telefone

    def to_string(self) -> str:
        return f"id_cliente: {self.get_id_cliente()} | Nome: {self.get_nome_cliente()} | telefone: {self.get_telefone()}"