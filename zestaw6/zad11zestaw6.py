def solve(tab, n, k, ile, iloczyn, i):

    if i==len(tab):
        if ile==n and iloczyn==k:
            return True
        else:
            return False
        
    
    return solve(tab, n, k, ile+1, iloczyn*tab[i], i+1)+solve(tab, n, k, ile, iloczyn, i+1)

if __name__=="__main__":

    n = int(input()); k = int(input())
    tab = [2,4,1,5,3,5,2,1]
    print(solve(tab, n, k, 0, 1, 0))

