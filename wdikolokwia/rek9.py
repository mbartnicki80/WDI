import math


def rek(tab, w, k, suma=0):
    n = len(tab)
    if w==n-1:
        return suma

    x = [-2, -1, 1, 2]
    y = [-1, -2, -2, -1]
    mini = math.inf
    for j in range(4):
        if -1<k+y[j]<n and -1<w+x[j]<n:
            if tab[k+y[j]][w+x[j]]==0:
                mini = min(rek(tab, w+x[j], k+y[j], suma+1), mini)
    return mini


def solve(tab):

    n = len(tab)
    mini = math.inf
    for i in range(n):
        if tab[0][i]==0:
            mini = min(rek(tab, 0, i), mini)
            
    if mini==math.inf:
        return None
    return mini



if __name__=="__main__":
    tab=[
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
    ]
    print(solve(tab))