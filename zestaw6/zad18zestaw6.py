from math import log10


def solve(tab, w, k, x, y):

    if w==7 and k==7:
        return True
    
    z=0
    for i in range(3):
        if w+x[i]<8 and k+y[i]<8 and tab[w][k]%10<tab[w+x[i]][k+y[i]]//(10**int(log10(tab[w+x[i]][k+y[i]]))):
            z|=solve(tab, w+x[i], k+y[i], x, y)

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
        [9,2,9,8,5,6,7,8]]
    x = [1, 1, 0]
    y = [0, 1, 1]
    print(solve(tab, w, k, x, y))