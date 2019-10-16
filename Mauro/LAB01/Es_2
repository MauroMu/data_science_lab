#Stesse considerazioni citate nell'esercizio 1

#Mancano gli extra (non li ho ancora guardati)

#PROGRAMMA:

#Dal prompt dei comandi eseguire: ---> wget "http://api.citybik.es/v2/networks/to-bike"-O tobike.json <---

#Attenzione a dove si salva il file scaricato. 


import json

with open("tobike.json") as f:
     obj = json.load(f)


V_stations = obj['network']['stations']    #Alcune chiavi del "dictionary" sono associate ad un valore che è a sua volta un "dictionary",
                                           #(come nel caso del valore di 'network'). Alla chiave 'Stations', invece, è associato, come valore,
                                           #un vettore composto da n 'dizionari' con n pari al numero delle stazioni e ognuno contenente tutte
                                           #le informazioni relative alla singola stazione

n=len(V_stations)

n_Onl=0
n_FreeBike=0
n_EmptySlots=0

for el in V_stations:

    valEmpty =el['empty_slots']
    valfree= el['free_bikes']
    n_FreeBike += int(valfree)
    n_EmptySlots += int(valEmpty)

    if el['extra']['status'] == 'online':
       n_Onl += 1
    

print('\nNumero di stazioni attive:',n_Onl)
print('\nNumero totale di bici libere:', n_FreeBike)
print("\nNumero totale di 'slot' vuoti:", n_EmptySlots)
