from math import log10


def solve(tab, w, k, x, y, parametr):

    if (w==7 and k==7) or (w==0 and k==0) or (w==0 and k==7) or (w==7 and k==0):
        return True
    
    z=0
    if parametr==1:
        for i in range(0, 3):
            if w+x[i]<8 and k+y[i]<8 and tab[w][k]%10<tab[w+x[i]][k+y[i]]//(10**int(log10(tab[w+x[i]][k+y[i]]))):
                z|=solve(tab, w+x[i], k+y[i], x, y, 1)
    if parametr==2:
        for i in range(3, 6):
            if w+x[i]<8 and k+y[i]<8 and tab[w][k]%10<tab[w+x[i]][k+y[i]]//(10**int(log10(tab[w+x[i]][k+y[i]]))):
                z|=solve(tab, w+x[i], k+y[i], x, y, 2)
    if parametr==3:
        for i in range(6, 9):
            if w+x[i]<8 and k+y[i]<8 and tab[w][k]%10<tab[w+x[i]][k+y[i]]//(10**int(log10(tab[w+x[i]][k+y[i]]))):
                z|=solve(tab, w+x[i], k+y[i], x, y, 3)
    if parametr==4:
        for i in range(9, 12):
            if w+x[i]<8 and k+y[i]<8 and tab[w][k]%10<tab[w+x[i]][k+y[i]]//(10**int(log10(tab[w+x[i]][k+y[i]]))):
                z|=solve(tab, w+x[i], k+y[i], x, y, 4)

    return z


if __name__=="__main__":

    w = int(input()); k = int(input())
    tab = [[1,2,1,4,5,6,7,1],
        [1,2,2,2,5,6,7,8],
        [1,2,3,3,5,6,7,8],
        [1,2,4,4,5,6,7,8],
        [1,2,5,6,5,6,7,8],
        [1,2,7,6,5,6,7,8],
        [1,8,3,7,5,6,7,8],
        [9,2,9,8,5,6,7,1]]
    x = [1, 1, 0, 1, 1, 0, -1, -1, 0, -1, -1, 0]
    y = [0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1]
    l=0
    l|=(solve(tab, w, k, x, y, 1))
    l|=(solve(tab, w, k, x, y, 2))
    l|=(solve(tab, w, k, x, y, 3))
    l|=(solve(tab, w, k, x, y, 4))
    print(l)
