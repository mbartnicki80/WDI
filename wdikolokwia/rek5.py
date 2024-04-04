def sumawiersz(tab):
    sumawiersz = [0]*len(tab)
    for i in range(len(tab)):
        suma = 0
        for j in range(len(tab)):
            suma += tab[i][j]
        sumawiersz[i] = suma
    return sumawiersz

def sumakol(tab):
    sumakol = [0]*len(tab)
    for i in range(len(tab)):
        suma = 0
        for j in range(len(tab)):
            suma += tab[j][i]
        sumakol[i] = suma
    return sumakol

def rek(tab, w1, k1, w2, k2, sumak, sumaw, suma):

    if w1==w2:
        nowasuma = sumak[k1]+sumak[k2]-tab[w1][k1]-tab[w2][k2]+sumaw[w1]
    elif k1==k2:
        nowasuma = sumaw[w1]+sumaw[w2]-tab[w1][k1]-tab[w2][k2]+sumak[k1]
    else:
        nowasuma = sumaw[w1]+sumaw[w2]+sumak[k1]+sumak[k2]-tab[w1][k1]-tab[w2][k2]-tab[w1][k2]-tab[w2][k1]

    if nowasuma>suma:
        return True
    return False

def solve(tab, w1, k1, w2, k2):
    sumak = sumakol(tab)
    sumaw = sumawiersz(tab)
    dl = len(tab)
    suma = 0

    if w1==w2:
        suma = sumak[k1]+sumak[k2]-tab[w1][k1]-tab[w2][k2]+sumaw[w1]
    elif k1==k2:
        suma = sumaw[w1]+sumaw[w2]-tab[w1][k1]-tab[w2][k2]+sumak[k1]
    else:
        suma = sumaw[w1]+sumaw[w2]+sumak[k1]+sumak[k2]-tab[w1][k1]-tab[w2][k2]-tab[w1][k2]-tab[w2][k1]
    
    w = False
    for i in range(dl):
        for j in range(dl):
            if w == False:
                w |= rek(tab, i, j, w2, k2, sumak, sumaw, suma)

    if w==True:
        return True
    
    for i in range(dl):
        for j in range(dl):
            if w == False:
                w |= rek(tab, w1, k1, i, j, sumak, sumaw, suma)
    return w

if __name__=="__main__":
    tab=[
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
    ]
    print(solve(tab, 1, 1, 4, 4))