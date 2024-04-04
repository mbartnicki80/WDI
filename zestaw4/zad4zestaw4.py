from random import randint


def sumykol(tab, a, n):
    
    suma = 0

    for i in range(n):
        suma += tab[i][a]

    return suma


def sumywiersz(tab, b, n):

    suma = 0
    
    for j in range(n):
            suma += tab[b][j]

    return suma


def iloraz(wiersz, kol, n):

    maksil = 0

    for i in range(n):
        for j in range(n):
            if kol[j]/wiersz[i]>maksil:
                maksil = kol[j]/wiersz[i]
                maxi = i
                maxj = j

    return maxi, maxj


if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [[randint(1, 100) for i in range(n)] for j in range(n)]
    wiersz = [0 for i in range(n)]
    kol = [0 for i in range(n)]

    for i in range(n):
        wiersz[i] = sumywiersz(tab, i, n)
    
    for j in range(n):
        kol[j] = sumykol(tab, j, n)
    
    for i in range(n):
        for j in range(n):
            print(tab[i][j], end=" ")
        print('')
        
    print(kol)
    print(wiersz)
    print(iloraz(wiersz, kol, n))