

class Facoltà:

    _nome:str
    _tipo_facoltà:str

    def __init__(self, nome:str, tipo_facolta:str):

        self._nome=nome
        self._tipo_facoltà=tipo_facolta

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nuovo_nome: str) -> None:
        self._nome = nuovo_nome

    def get_tipo_facoltà(self) -> str:
        return self._tipo_facoltà

    def set_tipo_facoltà(self, nuovo_tipo_facoltà: str) -> None:
        self._tipo_facoltà=nuovo_tipo_facoltà
    
    
