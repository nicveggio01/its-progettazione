from datetime import date
from custom_types import RealGTZ
from ClassCompagnia import Compagnia
from ClassAereoporto import Aereoporto


class Volo:

    _codice: str
    _durata_min: RealGTZ
    _compagnia:Compagnia
    _partenza:Aereoporto
    _arrivo:Aereoporto
    
    def __init__(self, codice: str, durata_min: RealGTZ, compagnia:Compagnia, partenza:Aereoporto, arrivo:Aereoporto)-> None:

        self._codice= codice
        self._durata_min= durata_min
        self._compagnia=compagnia
        self._arrivo=arrivo
        self._partenza=partenza

    def get_codice(self)-> str:
        return self._codice
    def set_codice(self, nuovo_codice:str)-> None:
        self._codice= nuovo_codice
    def get_compagnia(self)-> Compagnia:
        return self._compagnia
    def set_compagnia(self, nuova_compagnia)-> None:
        self._compagnia=nuova_compagnia
    def get_arrivo(self)-> Aereoporto:
        return self._arrivo
    def get_partenza(self)-> Aereoporto:
        return self._partenza
    def get_durata_min(self)-> RealGTZ:
        return self._durata_min
    def set_durata(self, nuova_durata:RealGTZ)-> None:

        if nuova_durata <= 0:
            raise ValueError("La durata del volo deve esere maggiore di zero.")
        
        self._durata_min= nuova_durata

    




    

