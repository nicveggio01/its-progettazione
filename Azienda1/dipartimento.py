from custom_types import Telefono, Indirizzo
from typing import List
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from impiegato import Impiegato

class Dipartimento:

    _nome: str # noto alla nascita
    _telefoni: set[Telefono] # [1..*] noto alla nascita
    _indirizzo: Indirizzo | None  # [0..1] possibilmente non noto alla nascita


    def __init__(self, nome: str, tel: Telefono, ind: Indirizzo|None) -> None:
        self.set_nome(nome)

        # opzione 1
        self._telefoni = set()
        self.add_telefono(tel)
        # opzione 2
        # self.set_telefoni({tel})

        self.set_indirizzo(ind)
        self._impiegati:List['Impiegato']=[]


    def nome(self) -> str:
        return self._nome

    def indirizzo(self) -> Indirizzo | None:
        return self._indirizzo

    def telefoni(self) -> frozenset[Telefono]:
        return frozenset(self._telefoni)

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_indirizzo(self, i: Indirizzo | None) -> None:
        self._indirizzo = i

    def add_telefono(self, telefono: Telefono) -> None:
        self._telefoni.add(telefono)

    def set_telefoni(self, telefoni: set[Telefono]) -> None:
        if not telefoni: # equivalente a len(telefoni) == 0
            raise ValueError("Il dipartimento deve avere almeno un numero di telefono")
        self._telefoni = telefoni

    def remove_telefono(self, telefono: Telefono) -> None:
        if len(self._telefoni) >= 2: # telefono è [1..*]!
            self._telefoni.remove(telefono)
        else:
            raise RuntimeError("Il dipartimento deve avere almeno un numero di telefono")
    def aggiungi_impiegato(self, nuovo_impiegato:'Impiegato'):
        if nuovo_impiegato not in self._impiegati:
            self._impiegati.append(nuovo_impiegato)
        else:
            print("L'impiegato è già nella lista dei dipendenti che ha afferito al dipartimento.")
    def rimuovi_impiegato(self, impiegato:'Impiegato')-> None:
        if impiegato not in self._impiegati:
            print("L'impiegato non afferisce al dipartimento per cui non è possibile rimuoverlo.")
        else:
            self._impiegati.remove(impiegato)

    def get_impiegati(self)-> List['Impiegato']:
        return self._impiegati
    

    def __str__(self):
        if self._indirizzo is None:
            ind_str: str = "senza sede"
        else:
            ind_str: str = f"con sede in {self.indirizzo()}"

        return f"Dipartimento '{self.nome()}' {ind_str} e numeri telefono: {self.telefoni()}"


if __name__ == "__main__":
    pass