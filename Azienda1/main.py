from custom_types import *
from datetime import date, timedelta
from progetto import Progetto
from impiegato import Impiegato
from coinvolto import Coinvolto
from dipartimento import Dipartimento
from afferenza import Afferenza
from direzione import  Direzione

tel1 = Telefono("3334445566")
tel2 = Telefono("3337778899")
ind = Indirizzo("Viale Cesare Pavese", "205b", CAP("00144"))

alice = Impiegato("Alice", "Alessi", date(1990, 12, 31), RealGEZ(18000))
print(f"Ho creato l'impiegata {alice.nome()} {alice.cognome()}")

bob = Impiegato("Bob", "Burnham", date(1997, 10, 11), RealGEZ(19000))
print(f"Ho creato l'impiegato {bob.nome()} {bob.cognome()}")

dip1 = Dipartimento("Vendite", tel1, ind)
print(f"Ho creato il dipartimento {dip1}")

dip2 = Dipartimento("Acquisti", tel2, None)
print(f"Ho creato il dipartimento {dip2}")

t = dip1.telefoni()
print("dip1.telefoni() = " + str(t))

dip1.add_telefono(Telefono("3481265413"))
print("dip1.telefoni() = " + str(dip1.telefoni()))

pegaso = Progetto("Pegaso", RealGEZ(50000))
print(f"Ho creato il progetto {pegaso.get_nome()}")
print(f"Il progetto ha un budjet di {pegaso.get_budget()}")

Coinvolto.add(alice, pegaso, date.today())
#ho praticamente fatto un ciclo per cercare il link giusto tra Alice e Pegaso
for link in alice.get_link_coinvolto():

    if link.progetto() == pegaso:

        print(f"Alice è stata coinvolta nel progetto {pegaso.get_nome()} in data: {link.data_inizio()}")

prometeo= Progetto("Prometeo", RealGEZ(100000))
print(f"Ho creato il progetto {prometeo.get_nome()}")
print(f"Il progetto ha un budjet di {prometeo.get_budget()}")

Coinvolto.add(bob, prometeo, date.today())
#ho praticamente fatto un ciclo per cercare il link giusto tra Bob e prometeo
for link in bob.get_link_coinvolto():
    if link.progetto()==prometeo:
        print(f"Bob è stato coinvolto nel progetto {prometeo.get_nome()} in data: {link.data_inizio()}")

niccolo= Impiegato("Niccolò", "Veggian", date(2001, 10, 12), RealGEZ(40000))
print(f"Ho creato l'impiegato {niccolo.nome()} {niccolo.cognome()}")

Coinvolto.add(niccolo, prometeo, date.today())

for link in niccolo.get_link_coinvolto():
    if link.progetto()== prometeo:
        print(f"Niccolò è stato coinvolto nel progetto {prometeo.get_nome()} in data: {link.data_inizio()}")

# Adesso mi creo due dipartimenti:

marketing= Dipartimento("Marketing", Telefono("0586680195") , Indirizzo("Viale Cesare Pavese", "132", 57023))
print(f"Ho creato un nuovo dipartimento {marketing.nome()}\ninfo:\n-Indirizzo:{marketing.indirizzo()}\nTelefono:{marketing.telefoni()}")

sviluppo= Dipartimento("Sviluppo", Telefono("0678923409"), Indirizzo("Viale Carlo Ginori", "105", 57023))
print(f"Ho creato un nuovo dipartimento {sviluppo.nome()}\ninfo:\n-Indirizzo:{sviluppo.indirizzo()}\nTelefono:{sviluppo.telefoni()}")

# Lavoriamo sull'afferenza

afferenza1= Afferenza(alice, sviluppo, date(2023,12,17))
print(f"Al dipartimento {afferenza1.get_dipartimento().nome()} ha afferito: {afferenza1.get_impiegato().nome()} in data: {afferenza1.get_data_afferenza()}")
sviluppo.aggiungi_impiegato(alice) # aggiungo alice alla lista self._impiegati=[]

# un dipendente può afferire ad uno ed un solo dipartimento

afferenza2=Afferenza(niccolo, sviluppo, date(2020, 10, 30))
print(f"Al dipartimento {afferenza2.get_dipartimento().nome()} ha afferito: {afferenza2.get_impiegato().nome()} in data: {afferenza2.get_data_afferenza()} ")
sviluppo.aggiungi_impiegato(niccolo) #aggiungo niccolo alla lista self._impiegati=[]

afferenza3= Afferenza(bob, marketing, date(2019, 3, 5))
print(f"Al dipartimento {afferenza3.get_dipartimento().nome()} ha afferito: {afferenza3.get_impiegato().nome()} in data: {afferenza3.get_data_afferenza()}")
marketing.aggiungi_impiegato(bob) #aggiungo bob alla lista self._impiegati=[] ma del Marketing


print(f"Dipartimento {sviluppo.nome()}----> Impiegati che afferiscono:")
for i in sviluppo.get_impiegati():
    print(f"{i.nome()}")

print(f"Dipartimento {marketing.nome()}----> Impiegati che afferiscono:")
for i in marketing.get_impiegati():
    print(f"{i.nome()}")

sviluppo.rimuovi_impiegato(niccolo) #rimuoviamo niccolo dai dipendenti che afferiscono a Sviluppo


print(f"Dipartimento {sviluppo.nome()}----> Impiegati che afferiscono:")
for i in sviluppo.get_impiegati():
    print(f"{i.nome()}") #Output ---> Alice

#Lavoriamo su Direzione-Direttore



daniele= Impiegato("Daniele", "Tafi", date(1985, 8, 29), RealGEZ(100000))
print(f"Ho creato l'impiegato {daniele.nome()}")

direttore_sviluppo= Direzione(daniele, sviluppo)
print(f"Il direttore del {direttore_sviluppo.get_dipartimento()} è {direttore_sviluppo.get_direttore().nome()} {direttore_sviluppo.get_direttore().cognome()}")
Direzione._registro_direttori[sviluppo]=daniele


sergio= Impiegato("Sergio", "De guidi", date(2004, 5, 20), RealGEZ(100000))
print(f"Ho creato l'impiegato {sergio.nome()}")

direttore_marketing= Direzione(sergio, marketing)
print(f"Il direttore del {direttore_marketing.get_dipartimento()} è {direttore_marketing.get_direttore().nome()} {direttore_marketing.get_direttore().cognome()}")
Direzione._registro_direttori[marketing]=sergio

print(f"Registro Direttori con i corrispettivi dipartimenti:")
print(" ")
for dip, d in Direzione.get_registro_direzioni().items():
    print(f"Il dipartimento {dip.nome()} ha come direttore {d.nome()} {d.cognome()}")

domenico=Impiegato("Domenico", "Candido", date(2005,5,22), RealGEZ(55000))

# proviamo ad assegnare un direttore a marketing dove c'è già sergio
# direttore_marketing=Direzione(domenico, marketing) #Output mi solleva l'errore come atteso


