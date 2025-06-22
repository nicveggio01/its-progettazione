
from custom_types import RealGEZ
from datetime import date
from typing import List


from typing import TYPE_CHECKING

if TYPE_CHECKING:
     from impiegato import Impiegato
     from coinvolto import Coinvolto


class Progetto:

    _nome:str
    _budget:RealGEZ
    _impiegati: List['Impiegato']
    

    def __init__(self, nome:str, budget:RealGEZ):

        self._nome=nome
        self._budget=budget
        self._coinvolgimenti:List['Coinvolto._link']=[]
    
    def get_nome(self)-> str:
        return self._nome
    
    def set_nome(self, nuovo_nome)-> None:
        self._nome= nuovo_nome
    
    def get_budget(self)-> RealGEZ:
        return self._budget
    
    def set_budget(self, nuovo_budget)-> None:
        self._budget= nuovo_budget
    
    def add_link_coinvolto(self, link:'Coinvolto._link')-> None:
        if link not in self._coinvolgimenti:
            self._coinvolgimenti.append(link)
    def get_link_coinvolto(self)->List['Coinvolto._link']:
        return self._coinvolgimenti
    def rimuovi_link_coinvolto(self, link:'Coinvolto._link')->None:
        if link in self._coinvolgimenti:
            self._coinvolgimenti.remove(link)
    

    
    


