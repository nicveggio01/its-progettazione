
from custom_types import RealGTZ
from typing import List
from ClassCittà import Città

class Compagnia:

    _nome: str
    _anno: RealGTZ
    _citta: Città

    def __init__(self, nome: str, anno: RealGTZ) -> None:
        self._nome = nome
        if anno <= 1900:
            raise ValueError("L'anno deve essere maggiore di 1900.")
        self._anno = anno
        self._citta = None

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nuovo_nome: str) -> None:
        self._nome = nuovo_nome

    def get_anno(self) -> RealGTZ:
        return self._anno

    def set_citta(self, citta: Città) -> None:
        self._citta = citta

    def get_citta(self) -> Città:
        return self._citta
