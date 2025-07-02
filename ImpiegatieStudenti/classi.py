
from __future__ import annotations
from custom_types import *
import frozendict



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
            self._maternita=maternita
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
        

        if is_responsabile:
            if ruolo != Ruolo.progettista:
                raise ValueError("Solo un progettista può essere responsabile di un progetto.")
            else:
                print(f"L'impiegato {self._nome} {self._cognome} partecipa al progetto come responsabile.")
        else:
            print(f"L'impiegato {self._nome} {self._cognome} non è il responsabile del progetto in quanto solo i progettisti responsabili possono.")

        
        if self._is_impiegato and not self._is_studente:
            print("La persona è un'impiegato")
        elif self.is_studente and not self._is_impiegato:
            raise ValueError("Una persona non può diventare studente o impiegato e viceversa.")
        else:
            print(f"La persona {self._nome} {self._cognome} non è ne uno studente ne un'impiegato")



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
        return f"Lo stipendio netto ammonta a {self._stipendio} euro per {self._nome} {self._cognome}"
    def set_stipendio(self, nuovo_stipendio:RealGEZ)->None:
        self._stipendio=nuovo_stipendio
    def __repr__(self):
        return f"{self._nome} {self._cognome}"

    
class Studente(Persona):

    _matricola:RealGTZ
    def __init__(self, *, nome, cognome, cf, genere, maternita = None, matricola:RealGTZ):
        super().__init__(nome=nome, cognome=cognome, cf=cf, genere=genere, maternita=maternita, is_studente=True, is_impiegato=False, posizione_mil=None)
        
        if matricola is None:
            raise ValueError("Errore la matricola è obbligatoria per uno studente.")
        else:
            self._matricola=matricola


    def getMatricola(self)->RealGTZ:
        return self._matricola
    
class Progetto:

    _nome:str
    lista_progetti:list[Progetto]=[]
    tutti_responsabili:set[Impiegato]=set()


    def __init__(self, nome:str, is_responsabile:bool,nome_responsabile:Impiegato):
        self._nome = nome
        self._is_responsabile= is_responsabile
        self._nome_responsabile= nome_responsabile._nome
        self._registri: dict[str, list[Impiegato]] = {}




        if self._is_responsabile:
              if nome_responsabile in Progetto.tutti_responsabili:
                print(f"Errore impossibile aggiungere {self._nome_responsabile} poichè è già responsabile di un progetto")
                return

              self._registri[self._nome] = [nome_responsabile]
              Progetto.tutti_responsabili.add(nome_responsabile)
              Progetto.lista_progetti.append(self)
        else:
            raise ValueError("Errore: l'impiegato non è responsabile!")


    def get_nome(self)->str:
        return self._nome

    
    def registro(self, nuovo_responsabile:Persona):
            
            if not isinstance(nuovo_responsabile, Impiegato):
                raise ValueError(f"Errore impossibile aggiungere la persona {nuovo_responsabile}  al progetto in quanto non è un impiegto.")
            if not nuovo_responsabile.getResponsabile():
                print(f"Impossibile aggiungere {nuovo_responsabile._nome} {nuovo_responsabile._cognome} alla lista responsabili.")
                return
            
            if nuovo_responsabile in Progetto.tutti_responsabili:
                print(f"Errore impossibile aggiungere {nuovo_responsabile}, è già responsabile di un progetto.")
                return
            
            if self._nome not in self._registri:
                self._registri[self._nome] = []
            self._registri[self._nome].append(nuovo_responsabile)
            Progetto.tutti_responsabili.add(nuovo_responsabile)
            Progetto.lista_progetti.append(self)
            
        
    

    def get_registri(self)->list:
        return self._registri
        
            
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


imp2= Impiegato(

    nome= "Domenico",
    cognome="Candido",
    cf=[CodiceFiscale("DCCNDN05R12C618X")],
    genere= Genere.uomo,
    posizione_mil=PosizioneMilitare("Riservista"),
    stipendio= RealGEZ(3000),
    ruolo=Ruolo.progettista,
    is_responsabile= True

)

imp3=Impiegato(
    nome="Sergio",
    cognome= "De Guidi",
    cf= [CodiceFiscale("SDGNDN04R12C420X")],
    genere= Genere.uomo,
    posizione_mil=PosizioneMilitare("Riservista"),
    stipendio=RealGEZ(4000),
    ruolo=Ruolo.progettista,
    is_responsabile=False
)

imp4= Impiegato(
    nome="Claudio",
    cognome="Benigni",
    cf= [CodiceFiscale("CBNNDN04R12C420X")],
    genere= Genere.uomo,
    posizione_mil=PosizioneMilitare("Riservista"),
    stipendio=RealGEZ(2100),
    ruolo= Ruolo.segretario,
    is_responsabile=False
)

s1= Studente(
    nome= "Anna",
    cognome= "Pepe",
    cf=[CodiceFiscale("APPAEP04R10C618Y")],
    genere= Genere.donna,
    maternita=RealGEZ(0),
    matricola=  RealGEZ(37025)
)

pegaso= Progetto(
    nome= "Pegaso",
    is_responsabile=True,
    nome_responsabile=imp
)

prometeo= Progetto(
    nome= "Prometeo",
    is_responsabile=True,
    nome_responsabile=imp
)


print(imp.getRuolo())
print(imp.get_stipendio())

try:
    imp2.diventaDirettore()
except ValueError:
    print(f"Errore, l'impiegato{imp2} non può diventare un direttore")

try:
    pegaso.registro(imp)
    print(pegaso.get_registri())
except ValueError:
     print(f"Errore impiegato {imp} non valido per questo progetto, non è un progettista.")

try:
    pegaso.registro(imp2)
    print(pegaso.get_registri())
except ValueError:
    print(f"Errore impiegato {imp2} non valido per questo progetto, non è un progettista.")
try:
    pegaso.registro(imp3)
    print(pegaso.get_registri())
except ValueError:
    print(f"Errore impiegato {imp3} non valido per questo progetto, non è un progettista.")

try:
    pegaso.registro(imp4)
    print(pegaso.get_registri())
except ValueError:
    print(f"Errore impiegato {imp4} non valido per questo progetto, non è un progettista.")

try:
    pegaso.registro(s1)
    print(pegaso.get_registri())
except ValueError:
    print(f"Errore impossibile aggiungere lo studente {s1._nome} {s1._cognome} al progetto.")

try:
    imp4.diventaDirettore()
    print(f"{imp4} è un nuovo direttore!")
except ValueError:
    print(f"Errore l'impiegato {imp4} non può divenatare direttore.")

try:
    imp3.diventaDirettore()
    print(f"{imp3} è un nuovo direttore!")
except ValueError:
    print(f"Errore l'impiegato {imp3} non può diventare un direttore.")

try:
    prometeo.registro(imp)
    print(prometeo.get_registri())
except ValueError:
    print(f"Errore impossibile aggiungere l'impiegato {imp} al progetto")















