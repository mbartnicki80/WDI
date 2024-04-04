def spirala(tab, n):

    i = 0; j = n-1
    l = 1
    while tab[i][j]==0:
        while (j<n-1 and tab[i][j+1]==0):
            tab[i][j] = l
            l += 1; j += 1
        while (i<n-1 and tab[i+1][j]==0):
            tab[i][j] = l
            l += 1; i += 1
        while (j>0 and tab[i][j-1]==0):
            tab[i][j] = l
            l += 1; j -= 1
        while (i>0 and tab[i-1][j]==0):
            tab[i][j] = l
            l += 1; i -= 1
        if l == n**2:
            tab[i][j] = l

    return tab

        

if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [[0 for i in range(n)] for j in range(n)]
    spirala(tab, n)
    #print(spirala(tab, n))