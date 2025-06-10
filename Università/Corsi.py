
from custom_types import RealGTZ
from Facoltà import Facoltà

class Corsi:

    _nome=str
    _codice=str
    _durata_in_ore=RealGTZ
    _appartiene:Facoltà

    def __init__(self, nome:str, codice:str, durata_in_ore:RealGTZ, appartiene:Facoltà):

        self._nome=nome
        self._codice=codice
        self._durata_in_ore=durata_in_ore
        self.set_appartiene(appartiene)
    
    
    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nuovo_nome: str) -> None:
        self._nome = nuovo_nome
    
    def get_codice(self) -> str:
        return self._codice

    def set_codice(self, nuovo_codice: str) -> None:
        self._codice=nuovo_codice
    
    def get_durata_in_ore(self) -> RealGTZ:
        return self._durata_in_ore

    def set_codice(self, nuova_durata_in_ore: RealGTZ) -> None:
        self._durata_in_ore=nuova_durata_in_ore
    
    def get_appartiene(self)-> Facoltà:
        return self._appartiene
    
    def set_appartiene(self, appartiene:Facoltà)-> None:
        self._appartiene=appartiene