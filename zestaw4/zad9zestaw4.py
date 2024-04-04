def funk(tab, n, k):

    for i in range(n-2):
        for j in range(n-2):
            e = j+2
            f = i+2
            while e<n and f<n:
                iloczyn = tab[i][j]*tab[i][e]*tab[f][j]*tab[f][e]
                if iloczyn==k:
                    return (f+i)/2, (e+j)/2
                f += 2
                e += 2
    
    return 0


if __name__=="__main__":

    n = int(input("Podaj n: "))
    k = int(input("Podaj k: "))
    tab = [[0,2,2,2,1],[1,0,3,2,2],[1,2,0,4,2],[1,2,3,0,5],[1,2,3,4,1]]

    for i in range(n):
        for j in range(n):
            print(tab[i][j], end=" ")
        print('')

    print(funk(tab, n, k))