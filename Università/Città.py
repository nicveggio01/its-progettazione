

from Regione import Regione

class Città:

    _nome:str
    _regione=Regione

    def __init__(self, nome:str, regione:Regione):
        self._nome=nome
        self._regione= regione
    
    def get_nome(self)-> str:
        return self._nome
    
    def set_nome(self, nuovo_nome)-> None:
        self._nome=nuovo_nome
    
    def get_regione(self) -> Regione:
        return self._regione

    def set_nazione(self, nuova_regione: Regione) -> None:
        self._regione = nuova_regione