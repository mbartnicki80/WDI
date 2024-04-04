def solve(tab, n, suma, ind, t):

    if ind==len(tab) or suma>=n:
        if suma==n:
            print(*t, sep='+')
            print()
            return
        else:
            return False
    
    solve(tab, n, suma+tab[ind], ind, t+[tab[ind]])
    solve(tab, n, suma, ind+1, t)

if __name__=="__main__":

    n = int(input())
    tab = [i for i in range(1, n)]
    t = []
    solve(tab, n, 0, 0, t)