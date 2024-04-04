import math

def rek(t, n):

    x = [1, -1, 1, -1, -2, -2, 2, 2]
    y = [2, 2, -2, -2, 1, -1, 1, -1]
    szachy = [[0 for i in range(n)] for j in range(n)]
    for i in t:
        szachy[i[0]][i[1]]=1
        for k in range(8):
            if -1<i[0]+y[k]<n and -1<i[1]+x[k]<n:
                szachy[i[0]+y[k]][i[1]+x[k]]=1
    
    suma = 0
    for i in range(n):
        for j in range(n):
            if szachy[i][j]==1:
                suma += 1
    return suma
        

def usun(tab, n):

    dl = len(tab)
    x = [1, -1, 1, -1, -2, -2, 2, 2]
    y = [2, 2, -2, -2, 1, -1, 1, -1]
    szachy = [[0 for i in range(n)] for j in range(n)]
    for i in tab:
        szachy[i[0]][i[1]]=1
        for k in range(8):
            if -1<i[0]+y[k]<n and -1<i[1]+x[k]<n:
                szachy[i[0]+y[k]][i[1]+x[k]]=1
    
    suma = 0
    for i in range(n):
        for j in range(n):
            if szachy[i][j]==1:
                suma += 1
                
    minsuma = math.inf
    for i in range(dl):
        t = []
        for j in range(dl):
            if j!=i:
                t.append(tab[j])
        minsuma = min(minsuma, rek(t, n))
            
    return suma-minsuma

if __name__=="__main__":
    tab=[(1, 0), (2, 3), (4, 1), (4, 5)]
    print(usun(tab, 6))