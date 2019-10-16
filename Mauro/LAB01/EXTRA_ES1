#Dal prompt: 1. Powershell 2. ---> wget "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data" -O iris.csv <---

#Attenzione a dove si salva il file scaricato. 

import csv
i=0
with open("iris.csv") as f:
    Lt=[]
    for cols in csv.reader(f):
        if len(cols)==5:
           Lt.append(cols)

n=len(Lt)
sum=[0,0,0,0]  
sumSetosa=[0,0,0,0]  
sumVersic=[0,0,0,0]  
sumVirgin=[0,0,0,0]  
media=[0,0,0,0] 
mediaSetosa=[0,0,0,0] 
mediaVersic=[0,0,0,0]  
mediaVirgin=[0,0,0,0] 
nSet=0
nVers=0
nVirg=0

q=4

for i in range(0,q):  

    for counter in range(n):
        
        if Lt[counter][q]=='Iris-setosa':
           sumSetosa[i] += float(Lt[counter][i])
        if Lt[counter][q]=='Iris-versicolor':
           sumVersic[i] += float(Lt[counter][i])  
        if Lt[counter][q]=='Iris-virginica':
           sumVirgin[i] += float(Lt[counter][i])

        sum[i] += float(Lt[counter][i])

        if i == 0:
           if Lt[counter][q]=='Iris-setosa':
              nSet += 1
           if Lt[counter][q]=='Iris-versicolor': 
              nVers += 1 
           if Lt[counter][q]=='Iris-virginica':
              nVirg += 1
        

for k in range(0,q):
    media[k]=sum[k]/n
    mediaSetosa[k]=sumSetosa[k]/nSet
    mediaVersic[k]=sumVersic[k]/nVers
    mediaVirgin[k]=sumVirgin[k]/nVirg

stdsum=[0,0,0,0]  
std=[0,0,0,0] 
stdsumSet=[0,0,0,0]  
stdSetosa=[0,0,0,0] 
stdsumVirgin=[0,0,0,0]  
stdVirgin=[0,0,0,0] 
stdsumVersic=[0,0,0,0]  
stdVersic=[0,0,0,0] 

for i in range(0,q):  
    for counter in range(n):
        if Lt[counter][q]=='Iris-setosa':
           stdsumSet[i] += pow((float(Lt[counter][i])-mediaSetosa[i]),2)
        if Lt[counter][q]=='Iris-versicolor':
           stdsumVersic[i] += pow((float(Lt[counter][i])-mediaVersic[i]),2)
        if Lt[counter][q]=='Iris-virginica':
           stdsumVirgin[i] += pow((float(Lt[counter][i])-mediaVirgin[i]),2)

        stdsum[i] += pow((float(Lt[counter][i])-media[i]),2)

for k in range(0,q):
    std[k]=pow((stdsum[k]/n),(1/2))
    stdSetosa[k]=pow((stdsumSet[k]/nSet),(1/2))
    stdVersic[k]=pow((stdsumVersic[k]/nVers),(1/2))
    stdVirgin[k]=pow((stdsumVirgin[k]/nVirg),(1/2))

print('\nMedia totale\n', media,'\nstd Totale\n', std)
print('\nMedia Iris-Setosa:\n', mediaSetosa,'\nstd Iris-Setosa:\n', stdSetosa)
print('\nMedia Iris-Versicolr:\n', mediaVersic,'\nstd Iris-Versicolr:\n', stdVersic)
print('\nMedia Iris-Virginica:\n', mediaVirgin,'\nstd Iris-Virginica:\n', stdVirgin)


############################EXTRA###########EXTRA########


""" EXTRA 4
4.
Per identificare al meglio la specie di iris a partire da uno dei quattro parmetri, considero gli intervalli centrati in ogni
valor medio e con una variazione di 3 sigma (u-3std, u+3std) (99%). Il miglior intervallo per descrivere ogni singola specie è quello la cui 
intersezione con i corrispondenti delle altre specie contiene il minor numero di valori. 

Per fare ciò, conviene implementare un metodo alternativo che conduce allo stesso risultato.
Per ogni coppia di liste, ne creo un'altra contenente il rapporto tra la somma delle std e la differenza (in modulo) dei valori medi. 
(Sarebbe come creare una lista contenente l'errore percentuale). """

best=[]
Listamedie=[mediaSetosa,mediaVersic,mediaVirgin]
Listastd=[stdSetosa, stdsumVersic, stdsumVirgin]
confronto=[]
app=[0,0,0,0]


for u in range(len(Listamedie)):
   
    for i in range(len(Listamedie)):
        if i != u:
           for k in range(4):
               app[k]= abs(float(float(Listastd[u][k])+float(Listastd[i][k])) / float(float(Listamedie[u][k])-float(Listamedie[i][k])))
           confronto.append(app)
    result= [0,0,0,0]

    for x in range(len(confronto)):
        for g in range(len(confronto[0])):
            result[g] += float(confronto[x][g])
    
    indicemin=0
    for y in range(len(result)-1):
        if float(result[y+1])<float(result[y]):
           indicemin = y+1
    
    print('\nper la categoria', u+1, 'il miglior parametro ha indice', indicemin+1)

""" Se viene fatto partire il programma si ottiene, che per tutte le specie, il parametro più caratterizzante è quello con indice 4. 
Ovvero la quarta colonna, corrispondente a "petal width, in cm". 

Se dovessi determinare la specie di Iris da uno dei parametri, sceglierei quest'ultimo. """


""" 

EXTRA 5

Basandoci su queste considerazioni posso classificare i tre vettori mostrati (allegati sotto):

5.2, 3.1, 4.0, 1.2
4.9, 2.5, 5.6, 2.0
5.4, 3.2, 1.9, 0.4
 
Confrontando con i valori medi associati al QUARTO parametro (petal width, in cm) ottengo:

1. Il primo probabilmente è riferito a Iris-Versicolor
2. Il secondo a Iris-Virginica
3. Il terzo a Iris-Setosa
 
 """

