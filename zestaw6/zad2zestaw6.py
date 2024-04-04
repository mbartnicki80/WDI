from math import log10, sqrt

def wg(liczba):

    dziel = 2
    suma = 0
    while (liczba>1):
        if liczba%dziel==0:
            suma+=1
            while (liczba%dziel==0):
                liczba/=dziel
        dziel+=1
    return suma

def waga(tab, t1, t2, t3, i):

    if i==len(tab):
        return t1==t2==t3
    return waga(tab, t1+wg(tab[i]), t2, t3, i+1) or waga(tab, t1, t2+wg(tab[i]), t3, i+1) or waga(tab, t1, t2, t3+wg(tab[i]), i+1)
    

if __name__=="__main__":

    tab = [2,6,30,2,6]
    print(waga(tab, t1=0, t2=0, t3=0, i=0))