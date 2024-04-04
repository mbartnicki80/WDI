from math import log10


def solve(tab, szukana, suma, i, uzyte):

    if i==8 or suma>=szukana:
        if szukana==suma:
            return True
        else:
            return False

    w = 0
    for j in range(8):
        for k in range(i):
            if uzyte[k]==j:
                break
        else:
            uzyte[i]=j
            w|=solve(tab, szukana, suma+tab[i][j], i+1, uzyte)
            uzyte[i]=-1
    
    return w

if __name__=="__main__":

    suma = int(input())
    tab = [[1,2,1,4,5,6,7,1],
        [1,2,2,2,5,6,7,8],
        [1,2,3,3,5,6,7,8],
        [1,2,4,4,5,6,7,8],
        [1,2,5,6,5,6,7,8],
        [1,2,7,6,5,6,7,8],
        [1,8,3,7,5,6,7,8],
        [9,2,9,8,5,6,7,1]]
    uzyte = [-1 for i in range(8)]
    print(solve(tab, suma, 0, 0, uzyte))