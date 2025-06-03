
from custom_types import RealGTZ
from typing import List
from ClassVolo import Volo
from ClassCittà import Città

class Compagnia:

    _nome: str
    _anno: RealGTZ
    _voli: List[Volo]
    _citta: Città

    def __init__(self, nome: str, anno: RealGTZ) -> None:
        self._nome = nome
        if anno <= 1900:
            raise ValueError("L'anno deve essere maggiore di 1900.")
        self._anno = anno
        self._voli = []
        self._citta = None

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nuovo_nome: str) -> None:
        self._nome = nuovo_nome

    def get_anno(self) -> RealGTZ:
        return self._anno

    def aggiungi_volo(self, volo: Volo) -> None:
        self._voli.append(volo)

    def get_volo(self) -> List[Volo]:
        return self._voli

    def rimuovi_volo(self, volo: Volo) -> None:
        if volo in self._voli:
            self._voli.remove(volo)

    def set_citta(self, citta: Città) -> None:
        self._citta = citta

    def get_citta(self) -> Città:
        return self._citta
