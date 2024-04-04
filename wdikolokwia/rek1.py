import math

def rek(w1, k1, tab, wieza, p1, suma=0):

    n = len(tab)-1
    if w1==n and k1==n and wieza==1:
        return suma
    if w1==n and k1==0 and wieza==2:
        return suma

    mins = math.inf
    #p1 = 1 - wiersz
    #p1 = 2 - kol
    if (p1==0 or p1==1) and wieza==1:
        for i in range(w1+1, n+1):
            if math.gcd(tab[w1][k1], tab[i][k1]) == 1:
                mins = min(rek(i, k1, tab, 1, 2, suma+1), mins)
    if (p1==0 or p1==2) and wieza==1:
        for i in range(k1+1, n+1):
            if math.gcd(tab[w1][k1], tab[w1][i]) == 1:
                mins = min(rek(w1, i, tab, 1, 1, suma+1), mins)

    if (p1==0 or p1==1) and wieza==2:
        for i in range(w1+1, n+1):
            if math.gcd(tab[w1][k1], tab[i][k1]) == 1:
                mins = min(rek(i, k1, tab, 2, 2, suma+1), mins)
    if (p1==0 or p1==2) and wieza==2:
        for i in range(k1-1, -1, -1):
            if math.gcd(tab[w1][k1], tab[w1][i]) == 1:
                mins = min(rek(w1, i, tab, 2, 1, suma+1), mins)

    return mins

def wieze(tab):

    n = len(tab)-1
    suma1 = rek(0, 0, tab, 1, 0)
    suma2 = rek(0, n, tab, 2, 0)

    if suma1==suma2:
        return 0
    elif suma1<suma2:
        return 1
    else:
        return 2

if __name__=="__main__":

    tab =[
        [5,2,3,4,5],
        [1,3,5,4,5],
        [1,2,7,4,5],
        [1,2,8,9,4],
        [5,2,3,4,4]
        ]
    print(wieze(tab))
