
from datetime import date
from custom_types import CodiceFiscale
from Corsi import Corsi

class Professori:
    
    _nome:str
    _codice_fiscale:CodiceFiscale
    _data_nascita:date
    _insegna: Corsi

    def __init__(self, nome:str, codice_fiscale:CodiceFiscale, data_nascita:date, insegna:Corsi):

        self._nome=nome
        self._codice_fiscale=codice_fiscale
        self._data_nascita=data_nascita
        self.set_insegna(insegna)

    
    def get_nome(self)-> str:
        return self._nome
    
    def set_nome(self, nuovo_nome)-> None:
        self._nome=nuovo_nome
    
    def get_codice_fiscale(self)-> CodiceFiscale:
        return self._codice_fiscale
    
    def get_data_nascita(self)-> date:
        return self._data_nascita
    
    def get_insegna(self)-> Corsi:
        return self._insegna
    def set_insegna(self, insegna:Corsi)-> None:
        self._insegna=insegna