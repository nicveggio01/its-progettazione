from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from impiegato import Impiegato
    from dipartimento import Dipartimento

class Direzione:
    _registro_direttori:dict['Dipartimento', 'Impiegato']={}
    class _link:

        _direttore:'Impiegato'
        _dipartimento:'Dipartimento'
        

    def __init__(self, direttore:'Impiegato', dipartimento:'Dipartimento')-> None:

        self._direttore= direttore
        self._dipartimento= dipartimento
        
        if dipartimento in Direzione._registro_direttori:
            raise ValueError(f"Il dipartimento {self._dipartimento} ha già un direttore.")
        else:
            Direzione._registro_direttori[dipartimento]= direttore

    def e_direttore(self, impiegato:'Impiegato')->bool:
        return self._direttore==impiegato
    def get_direttore(self)->'Impiegato':
        return self._direttore
    def set_direttore(self, nuovo_direttore:'Impiegato')->None:
        self._direttore=nuovo_direttore
        Direzione._registro_direttori[self._dipartimento]=nuovo_direttore
    def get_dipartimento(self)->'Dipartimento':
        return self._dipartimento
    def assegna_direttore(self, d:'Impiegato', dip:'Dipartimento'):
    
            if dip in Direzione._registro_direttori:
                print(f"Il dipartimento {dip} ha già un direttore.")
            else:
                Direzione._registro_direttori[dip]=d
    
    @classmethod
    def get_registro_direzioni(self)->dict['Dipartimento', 'Impiegato']:
        return self._registro_direttori
                
    
