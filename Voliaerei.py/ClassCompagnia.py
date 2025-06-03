from custom_types import RealGTZ
from typing import List
from ClassVolo import Volo

class Compagnia:

    _nome: str
    _anno:RealGTZ
    _voli:List[Volo]

    def __init__(self, nome:str, anno: RealGTZ) -> None:

        self._nome=nome
        if anno <= 1900:
            raise ValueError("L'anno deve essere maggiore di 1900.")
        self._anno=anno
        self._voli=[]
    
    def get_nome(self)-> str:
        return self._nome
    def set_nome(self, nuovo_nome:str)-> None:
        self._nome=nuovo_nome
    def get_anno(self)-> RealGTZ:
        return self._anno
    def aggiungi_volo(self, volo:Volo)-> None:
        self._voli.append(volo)
    def get_volo(self)->  Volo:
        return self
    def rimuovi_volo(self, volo:Volo)-> None:
        if volo in self._voli:
            self._voli.remove(volo)

    




