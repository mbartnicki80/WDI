from math import sqrt


def czypierw(ele):
    if ele<2:
        return False
    for i in range(2, int(sqrt(ele)+1)):
        if ele%i==0:
            return False
    return True

def solve(tab):
    dl = len(tab)
    x = [1, -1, 1, -1, -2, -2, 2, 2]
    y = [2, 2, -2, -2, 1, -1, 1, -1]

    for i in range(dl):
        for j in range(dl):
            for k in range(8):
                if -1<i+y[k]<dl and -1<j+x[k]<dl:
                    if czypierw(tab[i][j]+tab[i+y[k]][j+x[k]]):
                        return True
    return False

if __name__=="__main__":
    tab=[
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    print(solve(tab))