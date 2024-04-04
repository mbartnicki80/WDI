def funk(tab, n):

    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    maxsuma = 0
    maxi = -1
    maxj = -1

    for i in range(n):
        for j in range(n):
            suma = 0
            for k in range(8):
                if i+x[k]>-1 and i+x[k]<n and j+y[k]>-1 and j+y[k]<n:
                    suma += tab[i+x[k]][j+y[k]]
            if suma>maxsuma:
                maxsuma = suma
                maxi = i
                maxj = j

    return maxi+1, maxj+1

                

if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [[0,0,0],[0,1,1],[0,1,0]] #ma dac 3,3

    for i in range(n):
        for j in range(n):
            print(tab[i][j], end=" ")
        print('')

    print(funk(tab, n))