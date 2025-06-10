

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




