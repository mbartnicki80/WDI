def sumwiersz(T):
    n = len(T)
    sumw = [0]*n
    for i in range(n):
        suma = 0
        for j in range(n):
            if T[i][j]==1:
                suma+=1
        sumw[i] = suma
    return sumw

def sumkol(T):
    n = len(T)
    sumk = [0]*n
    for i in range(n):
        suma = 0
        for j in range(n):
            if T[j][i]==1:
                suma+=1
        sumk[i] = suma
    return sumk


def move(T):
    n = len(T)
    sumw = sumwiersz(T)
    sumk = sumkol(T)

    w1 = -1; k1 = -1; w2 = -1; k2 = -1
    for i in range(n):
        for j in range(n):
            if sumw[i]>1 and sumk[j]>1:
                w1= i
                k1 = j
                break
        if w1 != -1:
            break
    
    for i in range(n):
        for j in range(n):
            if sumw[i]==0 and sumk[j]==0:
                w2 = i
                k2 = j
                break
        if w2 != -1:
            break
    
    return (w1, k1), (w2, k2)

if __name__=="__main__":
    T = [
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    ]
    print(move(T))