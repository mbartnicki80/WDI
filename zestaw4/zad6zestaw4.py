from random import randint

def czysing(tab1, ele, n):

    licz = 0
    for i in range(n):
        for j in range(n):
            if tab1[i][j]>ele:
                break
            if tab1[i][j]==ele:
                licz += 1
            if licz==2:
                return 0

    return 1


def singleton(tab1, tab2, n):

    kol = [0 for i in range(n)]
    a = n; j = 0
    suma = 0

    while True:
        mini = 99999999
        ind = -1
        znaleziono = 0

        for i in range(n):
            if kol[i]<n and czysing(tab1, tab1[i][kol[i]], n) == 1 and tab1[i][kol[i]]<mini:
                znaleziono = 1
                mini = tab1[i][kol[i]]
                ind = i
        
        if znaleziono==0:
            for i in range(n):
                kol[i]+=1
                suma += 1
        else:
            kol[ind] += 1
            tab2[j] = mini
            j += 1
            a -= 1
            suma += 1

        if suma>=n**2:
            break

    return tab2

if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab1 = [[1,2,3],[2,3,4],[4,5,6]]
    tab2 = [0 for i in range(n**2)]

    for i in range(n):
        for j in range(n):
            print(tab1[i][j], end=" ")
        print('')

    print(singleton(tab1, tab2, n))