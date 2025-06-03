
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from ClassVolo import Volo  

class Aereoporto:

    _codice: str
    _nome: str
    _voli: List["Volo"]

    def __init__(self, codice: str, nome: str) -> None:
        self._codice = codice
        self._nome = nome
        self._voli = []

    def get_codice(self) -> str:
        return self._codice

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nuovo_nome: str) -> None:
        self._nome = nuovo_nome

    def get_voli(self) -> List["Volo"]:
        return self._voli

    def aggiungi_volo(self, volo: "Volo") -> None:
        self._voli.append(volo)

    def rimuovi_volo(self, volo: "Volo") -> None:
        if volo in self._voli:
            self._voli.remove(volo)
