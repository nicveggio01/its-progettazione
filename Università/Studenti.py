
from custom_types import RealGTZ
from custom_types import CodiceFiscale
from custom_types import Matricola
from datetime import date
from Corsi import Corsi
from Città import Città


class Studenti:

    _nome:str
    _codice_fiscale:CodiceFiscale
    _anno_iscr: RealGTZ
    _data_nascita:date
    _numero_matricola: Matricola
    _corsi_superati=dict[Corsi, RealGTZ]
    _voto:RealGTZ
    _iscritto:Corsi
    _città:Città

    def __init__(self, nome:str, codice_fiscale: CodiceFiscale, data_nascita:date, anno_iscr:RealGTZ, numero_matricola:Matricola, corsi_superati:dict[Corsi, RealGTZ], voto:RealGTZ, iscritto:Corsi, città:Città):

        self._nome=nome
        self._codice_fiscale=codice_fiscale
        self._anno_iscr=anno_iscr
        self._numero_matricola= numero_matricola
        self._data_nascita=data_nascita
        self._corsi_superati=  {}
        self._voto= voto
        self.set_iscritto(iscritto)
        self._città=città

    
    def get_nome(self)-> str:
        return self._nome

    def set_nome(self, nuovo_nome:str)-> None:
        self._nome= nuovo_nome
    
    def get_codice_fiscale(self)-> CodiceFiscale:
        return self._codice_fiscale
    
    def get_numero_matricola(self)->Matricola:
        return self._numero_matricola
    
    def get_data_nascita(self)-> date:
        return self._data_nascita

    def get_anno_iscr(self)-> RealGTZ:
        return self._anno_iscr
    
    def get_corso(self) -> str:
        return self._corso

    def set_corso(self, nuovo_corso:str) -> None:
        self._corso=nuovo_corso
    
    def get_corsi_superati(self)-> Corsi|None:
        
        if self._corsi_superati:
            return self._corsi_superati
        
        print("Non ci sono corsi superati")
    
    def set_corsi_superati(self, nuovo_corso_superato):

        if 18 <= self._voto <= 30:
            self._corsi_superati[nuovo_corso_superato]= self._voto
        else:
            raise ValueError("Voto non valido e corso non superato.")
    
    def get_iscritto(self)-> Corsi:
        return self._iscritto

    def set_iscritto(self, iscritto:Corsi)-> None:
        self._iscritto=iscritto
    
    def get_città(self)->Città:
        return self._città
    
    def set_città(self, nuova_città):
        self._città= nuova_città
    

