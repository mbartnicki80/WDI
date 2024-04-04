def solve(n):

    tab = [(0,0) for i in range(n**2)]
    t = [[0 for i in range(n)] for j in range(n)]
    x = [-2, -2, -1, -1, 1, 1, 2, 2]
    y = [1, -1, 2, -2, 2, -2, 1, -1]
    t[0][0]=1

    def skoczek(i, j, krok):

        tab[krok-1]=(i,j)

        if krok==n**2:
            for k in range(n**2):
                print(tab[k])
            exit()

        for k in range(8):
            if i+y[k]<n and i+y[k]>-1 and j+x[k]<n and j+x[k]>-1 and t[i+y[k]][j+x[k]]==0:
                t[i+y[k]][j+x[k]]=1
                skoczek(i+y[k], j+x[k], krok+1)
                t[i+y[k]][j+x[k]]=0

    skoczek(0, 0, 1)

if __name__=="__main__":

    n = int(input())
    solve(n)

