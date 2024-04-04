from math import sqrt
from random import randint

def czypierwsza(pierwsza):

    pierwsza[0] = pierwsza[1] = 0

    for i in range(2, int(sqrt(1000))):
        for j in range(i*i, 1000, i):
            pierwsza[j] = 0
    
    return pierwsza
        

if __name__=="__main__":

    tab = [randint(1,1000) for _ in range(100000)]
    tab1 = [0 for i in range(100000)]

    pierwsza = [1 for _ in range(1000)]
    czypierwsza(pierwsza)

    a = 1; b = 1
    while a+b<100000:
        a, b = b, a+b
        if pierwsza[tab[a]] == 1:
            print("NIE")
            exit()
        tab1[a] = 1

    for i in tab1:
        if tab1[i]==0 and pierwsza[tab[i]]==1:
            print("TAK")
            exit()

    print("NIE")
    
