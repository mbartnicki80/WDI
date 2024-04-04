def czyprzyj(tab1, ele):

    while ele>0:
        if tab1[ele%10]==0:
            return 0
        ele //= 10

    return 1
    

def rozbior(ele):

    tab = [0 for i in range(10)]

    while ele>0:
        tab[ele%10] += 1
        ele //= 10
    
    return tab


def funk(tab, n):

    x = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    suma = 0

    for i in range(n):
        for j in range(n):
            tab1 = rozbior(tab[i][j])
            for k in range(9): 
                if i+x[k]>-1 and i+x[k]<n and j+y[k]>-1 and j+y[k]<n:
                    if czyprzyj(tab1, tab[i+x[k]][j+y[k]])==0:
                        break
            else:
                suma += 1
    
    return suma
                

if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [[2,2,2,2,2],[2,0,3,2,2],[1,2,0,4,2],[1,2,3,0,5],[1,2,3,4,1]]

    for i in range(n):
        for j in range(n):
            print(tab[i][j], end=" ")
        print('')

    print(funk(tab, n))