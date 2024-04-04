from random import randint

if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [randint(0, 49)*2+1 for _ in range(n)]
    print(tab)

    r = tab[1]-tab[0]
    suma = 1
    maxsumadod = 1
    maxsumauj = 1

    for i in range(2, n):
        if tab[i]-tab[i-1]!=r:
            suma = 1
            r = tab[i]-tab[i-1]
        else:
            suma += 1
            if r>0 and suma>maxsumadod:
                maxsumadod = suma
            elif r<0 and suma>maxsumauj:
                maxsumauj = suma

    print(maxsumadod-maxsumauj)