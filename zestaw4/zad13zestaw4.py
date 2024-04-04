from math import sqrt


def czyzlozona(ele):

    for i in range(2, int(sqrt(ele))+1):
        if ele%i==0:
            return 0

    return 1


def funk(tab, n):

    for i in range(n):
        for j in range(n):
            znaleziono = 0
            for k in range(n):
                for l in range(n):
                    if (i == k and j == l) or tab[k][l]==0:
                        continue
                    if czyzlozona(tab[k][l]+tab[i][j])==1:
                            znaleziono = 1
                            break
                if znaleziono==1:
                    break
            if znaleziono==0:
                tab[i][j]=0
    
    return tab

                

if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [[2,3],[7,2]]

    for i in range(n):
        for j in range(n):
            print(tab[i][j], end=" ")
        print('')

    print(funk(tab, n))