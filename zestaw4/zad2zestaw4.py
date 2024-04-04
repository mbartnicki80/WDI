from random import randint


def niep(liczba):

    while liczba>0:
        if liczba%2 == 0:
            return 0
        liczba //= 10
    
    return 1

def wystep(tab, n):

    for i in range(n):
        for j in range(n):
            if niep(tab[i][j]) == 1:
                break
        else:
            return "NIE"

    return "TAK"

if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [[randint(1, 100) for i in range(n)] for j in range(n)]

    print(tab)
    print(wystep(tab, n))

