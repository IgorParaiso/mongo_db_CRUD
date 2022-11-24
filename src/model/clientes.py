class Cliente:
    def __init__(self,
                 cpf:int=None,
                 nome_cliente:str=None,
                 telefone:str=None):
        self.set_cpf(cpf)
        self.set_nome_cliente(nome_cliente)
        self.set_telefone(telefone)

    def set_cpf(self, cpf:int):
        self.cpf = cpf

    def set_nome_cliente(self, nome_cliente:str):
        self.nome_cliente = nome_cliente

    def set_telefone(self, telefone:int):
        self.telefone = telefone

    def get_cpf(self) -> int:
        return self.cpf

    def get_nome_cliente(self) -> str:
        return self.nome_cliente

    def get_telefone(self) -> str:
        return self.telefone

    def to_string(self) -> str:
        return f"cpf: {self.get_cpf()} | Nome: {self.get_nome_cliente()} | telefone: {self.get_telefone()}"