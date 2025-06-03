
from typing import Self, Type

class RealGTZ(float):


    def _new_(cls, v: int | float | str | bool | Self) -> Self:
        
        n: float = super()._new_(cls, v)

        if n > 0:
            return n

        raise ValueError(f"Il numero inserito {v}è negativo o zero!")
    
class RealGEZ(float):
    # Tipo di dato Reale >= 0

    def _new_(cls, v: int | float | str | bool | Self) -> Self:
        # Invoco il metodo new della superclasse, che è 'float'
        n: float = super()._new_(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v}ènegativo!")