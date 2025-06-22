from datetime import date
from custom_types import RealGEZ
from typing import List
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from coinvolto import Coinvolto

class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # <<immutable>>, noto alla nascita
    _stipendio: RealGEZ # noto alla nascita


    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGEZ) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self._coinvolgimenti:List['Coinvolto._link']=[]

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> RealGEZ:
        return self._stipendio
    def set_nome(self, n: str) -> None:
        self._nome: str = n
    def set_cognome(self, c: str) -> None:
        self._cognome: str = c
    def set_stipendio(self, s: RealGEZ) -> None:
        self._stipendio = s
    def add_link_coinvolto(self, link:'Coinvolto._link')-> None:
        if link not in self._coinvolgimenti:
            self._coinvolgimenti.append(link)
    def get_link_coinvolto(self)->List['Coinvolto._link']:
        return self._coinvolgimenti
    def rimuovi_link_coinvolto(self, link:'Coinvolto._link')->None:
        if link in self._coinvolgimenti:
            self._coinvolgimenti.remove(link)

        
