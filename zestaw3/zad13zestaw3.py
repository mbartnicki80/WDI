from random import randint


if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [randint(0,20) for _ in range(n)]

    maxsuma = 0
    for i in range(n):
        a = i
        suma = 0
        znaleziono = 0
        for j in range(n-1, a, -1):
            if tab[j]==tab[a]:
                a += 1
                suma += 1
                znaleziono = 1
                maxsuma = max(maxsuma, suma)
                continue
            if znaleziono==1 and tab[j]!=tab[a]:
                break

    print(maxsuma)