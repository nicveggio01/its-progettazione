
from __future__ import annotations
from custom_types import *



class Persona:
    _nome: str
    _cognome: str
    _cf: list[CodiceFiscale] # [1..*]
    _genere: Genere
    _maternita: IntGEZ # [0..1] - deve avere un valore se e solo se _genere = Genere.donna
    _posizione_mil: PosizioneMilitare | None # [0..1] da aggregazione, deve avere un valore se e solo se _genere = Genere.uomo
    is_impiegato:bool
    is_studente:bool

    def __init__(self, *, nome: str, cognome: str,
                 cf: list[CodiceFiscale],
                 genere: Genere,
                 maternita: IntGEZ|None=None, 
                 is_studente:bool,
                 is_impiegato:bool,
                posizione_mil:PosizioneMilitare) -> None:
        
        self._nome = nome
        self._cognome = cognome
        self._genere=genere
        self._maternita=maternita


        if not cf:
            raise ValueError("La persona deve avere almeno un codice fiscale!")

        if genere == Genere.donna:
            if maternita is None:
                raise ValueError("È obbligatorio fornire il numero di maternità per le donne")
            self.diventa_donna(maternita)
        if is_studente and is_impiegato:
            raise ValueError("Una persona non può essere sia studente che impiegato.")

        self._is_studente = is_studente
        self._is_impiegato = is_impiegato

        if genere== Genere.uomo:
           if posizione_mil is None:
               raise ValueError("La posizione militare deve essere definita.")
           self._posizione_mil=posizione_mil
        else:
            self._posizione_mil=None


    def diventa_donna(self, maternita: IntGEZ) -> None:
        if self._genere == Genere.donna:
            raise RuntimeError("La persona era già una donna!")
        self._genere = Genere.donna
        self.set_maternita(maternita)
        self.__dimentica_uomo()

    def __dimentica_uomo(self) -> None:
        # Questo metodo è privato perché non deve essere mai invocato dall'esterno, ma solo all'interno di questa classe
        self._posizione_mil = None

    def set_maternita(self, maternita: IntGEZ) -> None:
        if not self._genere == Genere.donna:
            raise RuntimeError("Gli uomini non hanno il numero di maternità!")


class Impiegato(Persona):

    def __init__(self, *, nome, cognome, cf, genere, maternita=None, stipendio: RealGEZ, ruolo: Ruolo, is_responsabile: bool, posizione_mil:PosizioneMilitare, responsabili:list[Impiegato]=[]):
        super().__init__(
            nome=nome,
            cognome=cognome,
            cf=cf,
            genere=genere,
            maternita=maternita,
            is_impiegato=True,
            is_studente=False,
            posizione_mil=posizione_mil
        )


        self._stipendio = stipendio
        self._ruolo = ruolo
        self._is_responsabile = is_responsabile
        self._responsabili=responsabili

        if ruolo == Ruolo.progettista:
            if is_responsabile:
                print("L'impiegato partecipa al progetto come responsabile.")
            else:
                print("L'impiegato non è il responsabile del progetto.")
        else:
            raise ValueError("L'impiegato non è un progettista")
        
        if self._is_impiegato and not self._is_studente:
            print("La persona è un'impiegato")
        elif self.is_studente and not self._is_impiegato:
            raise ValueError("Una persona non può diventare studente o impiegato e viceversa.")
        else:
            print("La persona non è ne uno studente ne un'impiegato")



    def getRuolo(self) -> str:
        return f" Il ruolo dell'impiegato è {self._ruolo}"
    
    def getResponsabile(self):
        if self._is_responsabile == True:
            return True
        else:
            return False
    
    def diventaSegretario(self) -> None:
        if self._is_responsabile == False :
            self._ruolo = Ruolo.segretario
        else:
            raise ValueError("Un responsabile non può diventare un segretario")
    
    def diventaDirettore(self) -> None:
        if self._ruolo == Ruolo.progettista and self._is_responsabile == False:
            self._ruolo = Ruolo.direttore
        else:
            raise ValueError("Un responsabile di un progetto non può diventare direttore.")
    
    def diventaProgettista(self) -> None:
        self._ruolo = Ruolo.progettista
    
    def diventaResponsabile(self) -> None:
        if self._ruolo == Ruolo.progettista:
            self._is_responsabile = True
        else:
            self._is_responsabile = False
    def get_stipendio(self)->RealGEZ:
        return f"Lo stipendio netto ammonta a {self._stipendio} euro"
    def set_stipendio(self, nuovo_stipendio:RealGEZ)->None:
        self._stipendio=nuovo_stipendio

    def get_responsabili(self)->list[Impiegato]:
        return self._responsabili
    
    def aggiungi_responsabile(self, nuovo_resp:Impiegato)->None:
        if self._is_responsabile:
            if nuovo_resp not in self._responsabili:
                self._responsabili.append(nuovo_resp)
            else:
                print(f"{nuovo_resp._nome}  {nuovo_resp._cognome} già nella lista dei responsabili")
        else:
            raise ValueError(f"Impossibile aggiungere l'impiegato{nuovo_resp._nome} {nuovo_resp._cognome}\n ---> Non è responsabile! ")

    def rimuovi_responsabile(self, resp:Impiegato)->None:
        if resp in self._responsabili:
            self._responsabili.remove(resp)
        else:
            print(f"{resp._nome} {resp._cognome} già rimosso oppure non si trova nella lista dei responsabili")


class Studente(Persona):

    _matricola:RealGTZ
    def __init__(self, *, nome, cognome, cf, genere, maternita = None, matricola:RealGTZ):
        super().__init__(nome=nome, cognome=cognome, cf=cf, genere=genere, maternita=maternita, is_studente=True, is_impiegato=False, posizione_mil=None)
        
        if matricola is None:
            raise ValueError("Errore la matricola è obbligatoria peruno studente.")
        else:
            self._matricola=matricola


    def getMatricola(self)->RealGTZ:
        return self._matricola
    
class Progetto:
    _nome:str

    def __init__(self, nome:str, is_responsabile:bool, nome_responsabile:Impiegato):
        self._nome = nome
        self._is_responsabile= is_responsabile
        self._nome_responsabile= nome_responsabile._nome

    def get_nome(self)->str:
        return self._nome
    
    def registro(self, registro:dict[Progetto, Impiegato]):

        self._registro=registro
        if self._is_responsabile:
            registro[self._nome]=self._nome_responsabile
        else:
            raise ValueError("Errore impossibile aggiungere l'impiegato al registro in quanto non è responsabile")
        
            


class PosizioneMilitare:
    _nome:str #immutabile
    def __init__(self, nome:str)->None:
        self._nome=nome
    def nome(self)->str:
        return self._nome
    def __str__(self)->str:
        return f"Posizione Militare: {self._nome}"

imp= Impiegato(
    nome="Niccolò",
    cognome= "Veggian",
    cf=[CodiceFiscale("VGGNCL01R12C415X")],
    genere= Genere.uomo,
    posizione_mil=PosizioneMilitare("Tenente"),
    stipendio=RealGEZ(2800),
    ruolo=Ruolo.progettista,
    is_responsabile=True
)

print(imp.getRuolo())
print(imp.get_stipendio())
# imp.diventaDirettore()
# print(imp.getRuolo())





