
from datetime import date
from custom_types import CodiceFiscale
from Corsi import Corsi
from Città import Città

class Professori:
    
    _nome:str
    _codice_fiscale:CodiceFiscale
    _data_nascita:date
    _insegna: Corsi
    _città:Città

    def __init__(self, nome:str, codice_fiscale:CodiceFiscale, data_nascita:date, insegna:Corsi, città:Città):

        self._nome=nome
        self._codice_fiscale=codice_fiscale
        self._data_nascita=data_nascita
        self.set_insegna(insegna)
        self._città=città

    
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
    
    def get_città(self)->Città:
        return self._città
    
    def set_città(self, nuova_città):
        self._città= nuova_città