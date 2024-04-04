import math

def krol(tab, i, k):

    if i == 7:
        return tab[i][k]
    
    y = [-1, 0, 1]
    minsuma = math.inf

    for j in range(3):
        if k+y[j]<8 and k+y[j]>-1:
            minsuma = min(krol(tab, i+1, k+y[j]), minsuma)

    return minsuma+tab[i][k]

if __name__=="__main__":

    k = int(input())
    tab = [
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8]
    ]
    print(krol(tab, 0, k))