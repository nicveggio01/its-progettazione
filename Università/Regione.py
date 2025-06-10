

class Regione:

    _nome:str

    def __init__(self, nome:str):
        self._nome=nome
    
    def get_nome(self)-> str:
        return self._nome
    
    def set_nome(self, nuovo_nome)-> None:
        self._nome=nuovo_nome