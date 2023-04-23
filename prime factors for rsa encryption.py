#!/usr/bin/python3 
#! Written by Abdelhamid
print('''La decomposition des nombres en facteurs premiers est tres importantes dans differents domaines.
Specialement en cryptogrraphie (eg:RSA encryption). 
Ceci est un programme simple que j'ai ecris afin de decomposer chaque nombre en ses facteurs premiers.
NB : J'ai utilise une 'recursive loop' qui est plus rapide qu' une double iteration sachant que O( nlog(n) ) >> O(n^2)
Ce qui laisse ce programme plus rapide que la plupart des autres. ''')

from math import sqrt
from sys import exit
facteurs_premiers= []
def dec_en_nbs_prem(nb):
    for x in range(2, int(sqrt(nb))+2):
        is_premier = 1
        for y in range(2, int(sqrt(x))+2):
            if x % y == 0:
                is_premier = 0
        if is_premier == 1 and nb % x == 0:
            facteurs_premiers.append(x)
            nb = nb // x
            dec_en_nbs_prem(nb)
            break
    if x == int(sqrt(nb))+1:
        facteurs_premiers.append(nb)


try:
    nb = int(input('Entrez le nb que vous voudriez decomposez en facteurs premiers: '))
    if nb <= 0:
        print('Svp entrez un nb str positif :)')
        exit()
    else:
        dec_en_nbs_prem(nb)
        facteurs_premiers = [str(h) for h in facteurs_premiers]
        print(f'{str(nb)} = ' + ' * '.join(facteurs_premiers))

except:
    print('Entrez svp un nb valide')
    exit()


