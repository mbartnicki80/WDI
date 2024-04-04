from math import sqrt

if __name__=="__main__":

    n = int(input("Podaj liczbę a: "))
    tab = [1 for i in range(n)]

    tab[0] = tab[1] = 0

    for i in range(2, int(sqrt(n)+1)):
        for j in range(i*i, n, i):
            tab[j] = 0

    for i in range(n):
        if tab[i]==1:
            print(i)
