import math


def rook(n, l, w=0, k=0, p=0, suma=0):

    if w==n-1 and k==n-1:
        return suma

    szachy = [[0 for i in range(n)] for i in range(n)]
    for i in l:
        szachy[i[0]][i[1]]=1

    minsuma = math.inf

    if p==0 or p==1:    #p1 == 1 - po wierszu
        for i in range(k+1, n):
            if szachy[w][i]==1:
                break
            minsuma = min(rook(n, l, w, i, 2, suma+1), minsuma)

    if p==0 or p==2:    #p1 == 2 - po kolumnie
        for i in range(w+1, n):
            if szachy[i][k]==1:
                break
            minsuma = min(rook(n, l, i, k, 1, suma+1), minsuma)

    if w==0 and k==0 and minsuma==math.inf:
        return None
    return minsuma

if __name__=="__main__":
    l=[(6,7), (7,6)]
    print(rook(8, l))