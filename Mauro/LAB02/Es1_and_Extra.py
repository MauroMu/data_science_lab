from random import gauss
import matplotlib.pyplot as plt
import csv

dataset=[]
with open("GLT.csv") as f:
    for cols in csv.reader(f):
        dataset.append(cols)

###Punto 2: 'Pulizia' dati

for n in range(len(dataset)):
    flag=0
    if dataset[n][1] == "":
        i = n
        while dataset[i][1] == "" and flag==0:
            if i != (len(dataset)-1):
               if dataset[n][3] == dataset[i+1][3]:
                  i += 1
               else:
                  flag=1
            else:
                flag=1
        
        if flag==0:
            if n==0 or (n!=0 and dataset[n-1][3] != dataset[n][3]): 
                dataset[n][1] = (0 + float(dataset[i][1])) / 2
            else:
                dataset[n][1] = (float(dataset[n-1][1]) + float(dataset[i][1])) / 2
        else:
            if n == 0 or (n!=0 and dataset[n-1][3] != dataset[n][3]):
                print('Error: nessun valore presente per la città:', dataset[n][3])
            else:
                dataset[n][1] = (float(dataset[n-1][1]) + 0) / 2


### Adesso AverageTemperature in dataset è corretto
###Punto 3: Definire funzione che restituisce le Ntemperature più fredde e le N più calde, avendo N e city come input

def rank(N, city):
    l_rank=[-1000]
    for el in dataset:
        if el[3] == city:
           u=0
           for k in range(len(l_rank)):
               if float(el[1]) >= float(l_rank[k]):
                   l_rank.insert(k, round(float(el[1]), 3))
                   u=1 
                   break
           if u==0:  ## Non c'è bisogno di questo if avendo inizializzato l_rank= [-1000]
              l_rank.append(el[1]) ## cioè le temperature saranno sempre maggori di -1000, quindi u non rimarrà mai zero 
    
    # l_rank= [float(el[1]) for el in dataset if el[1] !='AverageTemperature' and el[3]==city]
    # l_rank.sort()
    # l_rank.reverse() ###Questi tre comandi creano un vettore con temperature ordinate (decrescente) in poche righe (Attenti al print. elimina ultimo valore)
    
    lun=len(l_rank)
    print('\nLe', N, 'temperature più calde a', city, 'sono:\n', l_rank[0:N])
    print('\nLe', N, 'temperature più fredde a', city, 'sono:\n', l_rank[(lun-N-1):-1]) ##ignoro -1000 poiché aggiunto da me alla fine della lista

rank(7, 'Abidjan')

"""Punto 4 - EXTRA: Let’s search for other anomalies in data distribution with the help of matplotlib. Plot the distribution
of the average land temperatures for Rome and Bangkok using the aforementioned histogram
plotting function. """

#Potrei introdurre questi comandi nel for iniziale. Ma sviluppo il quarto punto separatamente

List_Rome=[]
List_Bangkok=[]

for el in dataset:
    if el[3] == 'Rome':
        List_Rome.append(float(el[1]))
    if el[3]== 'Bangkok':
        List_Bangkok.append(float(el[1]))

plt.hist(List_Rome)
plt.hist(List_Bangkok)
plt.title('Temperature distribution for Rome (Celsius) and Bangkok (Fhrenehit)')  
plt.show()

#RISPOSTA: E' decisamente improbabile che, durante tutto l'arco temporale, i sensori fossero danneggiati.
##Probabilmente i risultati per bangkok sono forniti in un'altra unità di misura. Probabilmente si usa la scala Fahrenheit.
## °C=(°F-32)/1.8
##Basta aplicare la converione  ogni elemento di List_Bangkok per ottenere la misura in gradi Celsius

##PUNTO 5 EXTRA - Le considerazioni erano esatte. Ripeto lo stesso ciclo for correggendo le temperature di Bangkok:


List_Rome_Celsius=[]
List_Bangkok_Celsius=[]
for el in dataset: #SINTESI: List_Rome..= [float(el[1]) for el in dataset if el[1] !='AverageTemperature' and el[3]==Rome]
    if el[3] == 'Rome':
        List_Rome_Celsius.append(float(el[1]))
    if el[3]== 'Bangkok':
        List_Bangkok_Celsius.append(((float(el[1])-32)/1.8))

plt.hist(List_Rome_Celsius)
plt.hist(List_Bangkok_Celsius)
plt.title('Temperature distribution for Rome(blu) and Bangkok(Orange)')  
plt.show()
