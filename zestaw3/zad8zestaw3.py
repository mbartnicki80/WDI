from math import sqrt

def czypierw(tablyca):

    tablyca[0] = tablyca[1] = 0
    for i in range(2, int(sqrt(100000))):
        for j in range(i*i, 100000, i):
            tablyca[j] = 1

    return tablyca

def przejscie(tab, tab1, pierwsza):

    for i in range(n):
        if tab1[i]==1:
            a = tab[i]
            dzielnik = 2

            while a>1:
                if a%dzielnik==0:
                    while a%dzielnik==0:
                        a //= dzielnik 
                    if pierwsza[dzielnik]==1 and i+dzielnik<n:
                        tab1[i+dzielnik]=1
                else:
                    dzielnik += 1
    return tab1

if __name__=="__main__":

    n = int(input("podaj n: "))
    tab = [0 for i in range(n)]
    for i in range(n):
        tab[i] = int(input("Podaj element tablicy: "))

    tab1 = [0 for i in range(n)]
    tab1[0] = 1

    

    pierwsza = [1 for i in range(100000)]
    czypierw(pierwsza)
    przejscie(tab, tab1, pierwsza)
    
    print(tab1[n-1])
