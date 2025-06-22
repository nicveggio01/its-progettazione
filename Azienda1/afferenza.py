from datetime import date
from typing import List

from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from impiegato import Impiegato
    from dipartimento import Dipartimento



class Afferenza:

    _data_afferenza:date

    def __init__(self, impiegato:'Impiegato', dipartimento:'Dipartimento', data_afferenza:date):

        self._impiegato= impiegato
        self._dipartimento= dipartimento
        self.set_data_afferenza(data_afferenza)
     
    
    def get_impiegato(self)->'Impiegato':
        return self._impiegato
    def set_impiegato(self, nuovo_impiegato:'Impiegato')->None:
        self._impiegato=nuovo_impiegato
    def get_dipartimento(self)-> 'Dipartimento':
        return self._dipartimento
    def set_dipartimento(self, nuovo_dipartimento:'Dipartimento')-> None:
        self._dipartimento= nuovo_dipartimento
    def get_data_afferenza(self)-> date:
        return self._data_afferenza
    def get_impiegati(self)->  List['Impiegato']:
        return self._impiegati
  
    def set_data_afferenza(self, data_afferenza: date)->None:
        if not isinstance(data_afferenza, date):
            raise ValueError("Errore la data afferenza non è di tipo Date.")
        self._data_afferenza=data_afferenza
    






