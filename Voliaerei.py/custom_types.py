
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
