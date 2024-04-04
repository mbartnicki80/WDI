def solve(tab, n):

    if n==1:
        return tab[0][0]
    
    sum = 0
    for i in range(n):
        t = [[0 for _ in range(n-1)] for _ in range(n-1)]
        a = 0; b = 0
        for k in range(1, n):
            for l in range(n):
                if l!=i:
                    t[a][b]=tab[k][l]
                    b = (b+1)%(n-1)
                    if b==0:
                        a += 1
        sum += tab[0][i]*((-1)**(2+i))*solve(t, n-1)
    
    return sum


if __name__=="__main__":

    n = int(input())
    tab = [[1,-1,2,4],[0,1,0,3],[5,7,-2,0],[2,0,-1,4]]
    print(solve(tab, n))