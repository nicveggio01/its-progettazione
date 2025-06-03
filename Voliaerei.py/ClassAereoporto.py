from typing import List, TYPE_CHECKING
from custom_types import RealGEZ
from ClassNazione import Nazione

if TYPE_CHECKING:
    from ClassAereoporto import Aereoporto
    from ClassCompagnia import Compagnia

class Città:

    _nome: str
    _abitanti: RealGEZ
    _nazione: Nazione
    _compagnia: List["Compagnia"]
    _aereoporto: List["Aereoporto"]

    def __init__(self, nome: str, abitanti: RealGEZ, nazione: Nazione) -> None:
        self.set_abitanti(abitanti)
        self._nome = nome
        self._nazione = nazione
        self._compagnia = []
        self._aereoporto = []

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nuovo_nome: str) -> None:
        self._nome = nuovo_nome

    def get_nazione(self) -> Nazione:
        return self._nazione

    def set_nazione(self, nuova_nazione: Nazione) -> None:
        self._nazione = nuova_nazione

    def set_abitanti(self, nuovi_abitanti: RealGEZ) -> None:
        if nuovi_abitanti < 0:
            raise ValueError("Per gli abitanti non possiamo avere un valore negativo.")
        self._abitanti = nuovi_abitanti

    def get_abitanti(self) -> RealGEZ:
        return self._abitanti

    def get_compagnia(self) -> List["Compagnia"]:
        return self._compagnia

    def aggiungi_compagnia(self, compagnia: "Compagnia") -> None:
        self._compagnia.append(compagnia)

    def rimuovi_compagnia(self, compagnia: "Compagnia") -> None:
        if compagnia in self._compagnia:
            self._compagnia.remove(compagnia)

    def get_aereoporto(self) -> List["Aereoporto"]:
        return self._aereoporto

    def aggiungi_aereoporto(self, aereoporto: "Aereoporto") -> None:
        self._aereoporto.append(aereoporto)

    def rimuovi_aereoporto(self, aereoporto: "Aereoporto") -> None:
        if aereoporto in self._aereoporto:
            self._aereoporto.remove(aereoporto)

