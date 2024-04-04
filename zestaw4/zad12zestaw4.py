from math import sqrt


def czyzlozona(ele):

    for i in range(2, int(sqrt(ele))+1):
        if ele%i==0:
            return 0

    return 1


def funk(tab, n):

    x = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

    sumapop = 0

    for z in range(n):
        suma = 0

        for i in range(n):
            for j in range(n):
                for k in range(9): 
                    if i+x[k]>-1 and i+x[k]<n and j+y[k]>-1 and j+y[k]<n:
                        if czyzlozona(tab[z][i+x[k]][j+y[k]])==0:
                            break
                else:
                    suma += 1
         
        if z!=0 and suma!=sumapop:
            return False
        sumapop=suma
        
    return True
                

if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [[1,2],[1,2]]

    for i in range(n):
        for j in range(n):
            print(tab[i][j], end=" ")
        print('')

    print(funk(tab, n))