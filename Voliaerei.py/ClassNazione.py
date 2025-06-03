
from typing import List
from ClassCittà import Città


class Nazione:

    _nome:str
    _città:List[Città]
    

    def __init__(self, nome:str, ):
        self._nome=nome
        self._città=[]
    
    def get_nome(self) -> str:
        return self._nome
    def set_nome(self, nuovo_nome:str)-> None:
        self._nome=nuovo_nome
    def get_città(self)-> Città:
        return self._città
    def aggiugi_città(self, città:Città)-> None:
        self._città.append(città)
    def rimuovi_città(self, città:Città)-> None:
        if città in self._città:
            self._città.remove(città)
