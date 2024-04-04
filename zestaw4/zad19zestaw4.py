def funk(tab, n, iloczyn):

    x = [2, 1, -1, -2]
    y = [1, 2, 2, 1]
    suma = 0

    for i in range(n):
        for j in range(n):
            for k in range(4):
                if i+y[k]<n and i+y[k]>-1 and j+x[k]>-1 and j+x[k]<n:
                    if tab[i][j]*tab[i+y[k]][j+x[k]]==iloczyn:
                        suma += 1

    return suma

    
if __name__=="__main__":

    tab = [[2,4,0],[0,0,4],[2,0,2]] # ma dac 4
    iloczyn = 8
    print(funk(tab, len(tab), iloczyn))