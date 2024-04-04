def sumywiersz(tab, n):

    wiersz = [0 for i in range(n)]

    for i in range(n):
        suma = 0
        for j in range(n):
            suma += tab[i][j]
        wiersz[i] = suma
    
    return wiersz


def sumykol(tab, n):

    kol = [0 for i in range(n)]

    for i in range(n):
        suma = 0
        for j in range(n):
            suma += tab[j][i]
        kol[i] = suma
    
    return kol

def funk(tab, n):

    wiersz = sumywiersz(tab, n)
    kol = sumykol(tab, n)

    maxsuma = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                suma = 0
                for l in range(n):
                    if i==k and j==l: continue
                    if i==k: 
                        suma = kol[j]+kol[l]+wiersz[i]-tab[i][j]-tab[k][l]
                    elif j==l:
                        suma = wiersz[i]+wiersz[k]+kol[j]-tab[i][j]-tab[k][l]
                    else:
                        suma = wiersz[i]+kol[j]-2*tab[i][j]+wiersz[k]+kol[l]-2*tab[k][l]-tab[k][j]-tab[i][l]
                    maxsuma = max(maxsuma, suma)
    return maxsuma

if __name__=="__main__":

    tab = [[4,4,0],[4,0,4],[4,4,4]] # ma dac 24

    print(funk(tab, len(tab)))