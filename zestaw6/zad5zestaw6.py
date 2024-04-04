from math import sqrt


def czypierwsza(l):

    if l==0 or l==1:
        return 0
    for i in range(2, int(sqrt(l))+1):
        if l%i==0:
            return 0
    return 1

def bin(tab, pocz, kon):

    liczba = 0
    pot = 0
    for i in range(kon, pocz-1, -1):
        liczba+=tab[i]*(2**pot)
        pot += 1
    return czypierwsza(liczba)

def solve(t, n, pocz, ind):
    
    if ind==n-1:
        if bin(t, pocz, ind)==1:
            return True
        return False

    w = solve(t, n, pocz, ind+1)
    if bin(t, pocz, ind):
       w|=solve(t, n, ind+1, ind+1)
    
    return w
    
if __name__=="__main__":

    t = [1,1,1,0,1,1]
    print(solve(t, len(t), 0, 0))