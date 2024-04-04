def geo(tab, a, b):

    q = tab[a][b]/tab[a+1][b+1]

    while a+2<n and b+2<n:
        a += 1
        b += 1
        if tab[a][b]/tab[a+1][b+1]!=q:
            return 0
    
    return 1


def funk(tab1, n):

    maksi = 0
    for i in range(n-2):
        if geo(tab1, i, 0):
            maksi = max(maksi, n-i)

    for j in range(n-2):
        if geo(tab1, 0, j):
            maksi = max(maksi, n-j)
        
    return maksi


if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab1 = [[2,1,1],[2,4,8],[3,1,8]]

    for i in range(n):
        for j in range(n):
            print(tab1[i][j], end=" ")
        print('')

    print(funk(tab1, n))