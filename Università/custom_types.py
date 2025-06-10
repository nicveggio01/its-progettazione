

from typing import Self

class RealGTZ(float):
    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        n: float = super().__new__(cls, v)
        if n > 0:
            return n
        raise ValueError(f"Il numero inserito {v} è negativo o zero!")

class RealGEZ(float):
    
    def __new__(cls, v: int | float | str | bool | Self) -> Self:
        n: float = super().__new__(cls, v)  
        if n >= 0:
            return n
        raise ValueError(f"Il numero inserito {v} è negativo!")

import re

class CodiceFiscale:
    def __init__(self, codice):
        if not self._valida_codice(codice):
            raise ValueError("Codice Fiscale non valido.")
        self.codice = codice.upper()

    def __str__(self):
        return self.codice

    def __eq__(self, other):
        if isinstance(other, CodiceFiscale):
            return self.codice == other.codice
        return False

    def __len__(self):
        return len(self.codice)

    @staticmethod
    def _valida_codice(codice):
        pattern = r"^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$"
        return bool(re.match(pattern, codice.upper()))

    def is_valid(self):
        return self._valida_codice(self.codice)
    
class Matricola(int):
    def __new__(cls, value):
        if not isinstance(value, int):
            raise TypeError("La matricola deve essere un intero.")
        if value <= 0:
            raise ValueError("La matricola deve essere un numero positivo.")
        if len(str(value)) < 6:
            raise ValueError("La matricola deve avere almeno 6 cifre.")
        return int.__new__(cls, value)





