#Non ho avuto tempo di fare gli extra, quindi non sono presenti.
#Probabilmente non è un programma molto compatto e ho definito troppe variabili. 
#Perdonatemi l'ignoranza, ho cercato di fare le cose in modo logico senza cosiderare troppo il codice.

#PROGRAMMA:

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

print('\nVerifica:\n', nSet+nVirg+nVers, '\n', n)
