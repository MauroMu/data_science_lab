#Stesse considerazioni esercizi precedenti
#Non ho ancora guardato gli extra

#PROGRAMMA:

#Scaricare da browser o prompt il file csv. Link: https://raw.githubusercontent.com/dbdmg/data-science-lab/master/datasets/mnist_test.csv

import csv

with open("MNIST.csv") as f:
     Lt=[]
     for cols in csv.reader(f):
         if len(cols)==785:
            Lt.append(cols)

n=len(Lt)

def stampa(k):

    if k<1 or k>n:
       print('Error: Must be 1 <= k <=',n)

    elif k>=1 and k<=n:
         k -= 1
         for i in range(0,27):
            print('\n')
            #listastampa=[]
            for u in range(1,28):

                if int(Lt[k][u+i*28])>=0 and int(Lt[k][u+i*28])<64:
                   print(' ', end='')
                if int(Lt[k][u+i*28])>=64 and int(Lt[k][u+i*28])<128:
                   print('.', end='')
                if int(Lt[k][u+i*28])>=128 and int(Lt[k][u+i*28])<192:
                   print('*', end='')
                if int(Lt[k][u+i*28])>=192 and int(Lt[k][u+i*28])<256:
                   print('#', end='')
    print('\n', Lt[k][0])


print(f"{stampa(170)}")



##Distanza Euclidea

lista_distanza=[]
lista_distanza.append(Lt[25])
lista_distanza.append(Lt[29])
lista_distanza.append(Lt[31])
lista_distanza.append(Lt[34])

print(len(lista_distanza))
for u in range(0, len(lista_distanza)-1):
    for g in range(u+1, len(lista_distanza)):
        x=0

        for i in range(len(Lt[1])):
            x += (int(Lt[u][i])-int(Lt[g][i]))**2

        dist = pow(x, (1/2))
        print('Distanza tra il vettore', u, 'e il vettore', g, ':\n', dist)
