
from ClassVolo import Volo
from ClassCompagnia import Compagnia
from ClassAereoporto import Aereoporto
from custom_types import RealGTZ
from ClassCittà import Città
from ClassNazione import Nazione


nazione = Nazione("Italia")
città = Città("Roma", 2873000, nazione)
aeroporto_partenza = Aereoporto("FCO", "Leonardo da Vinci")
aeroporto_arrivo = Aereoporto("LIN", "Linate")

compagnia = Compagnia("Alitalia", RealGTZ(2001))
compagnia.set_citta(città)

volo = Volo("AZ123", RealGTZ(90), compagnia, aeroporto_partenza, aeroporto_arrivo)
print("Codice volo:", volo.get_codice())
print("Durata (minuti):", volo.get_durata_min())
print("Compagnia:", volo.get_compagnia().get_nome())
print("Città di origine della compagnia:", compagnia.get_citta().get_nome())
print("Partenza da:", volo.get_partenza().get_nome(), "-", volo.get_partenza().get_codice())
print("Arrivo a:", volo.get_arrivo().get_nome(), "-", volo.get_arrivo().get_codice())
