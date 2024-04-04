def solve(tab, n, k, ile, iloczyn, i, t):

    if i==len(tab):
        if ile==n and iloczyn==k:
            print(t)
            return
        else:
            return False
        
    
    solve(tab, n, k, ile+1, iloczyn*tab[i], i+1, t+[tab[i]])
    solve(tab, n, k, ile, iloczyn, i+1, t)

if __name__=="__main__":

    n = int(input()); k = int(input())
    tab = [2,4,1,5,3,5,2,1]
    t = []
    solve(tab, n, k, 0, 1, 0, t)

