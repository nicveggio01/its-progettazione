

from datetime import date
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from impiegato import Impiegato
    from progetto import Progetto



class Coinvolto:
    @classmethod
    def add(cls, impiegato:'Impiegato', progetto:'Progetto', data_inizio:date)-> None:
        l=cls._link(impiegato, progetto, data_inizio)
        # crae il link l (impiegato, progetto)
        impiegato.add_link_coinvolto(l)
        progetto.add_link_coinvolto(l)

    class _link:

        _impiegato:'Impiegato' # immutabile
        _progetto:'Progetto'# immutabile
        _data_inizio: date

        def __init__(self, i:'Impiegato', p:'Progetto', d:date):
            self._impiegato:'Impiegato'=i
            self._progetto:'Progetto'=p
            self._data_inizio:date=d

        def impiegato(self)->'Impiegato':
            return self._impiegato
        def progetto(self)-> 'Progetto':
            return self._progetto
        def data_inizio(self)-> date:
            return self._data_inizio
        def is_coinvolto(self)-> bool:

            if self._impiegato not in 'Progetto':
                return False
            else:
                return True
            

        
        