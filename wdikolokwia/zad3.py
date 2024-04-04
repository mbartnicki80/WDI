from math import log10, sqrt

def pierwsza(l):

    for i in range(2, int(sqrt(l))+1):
        if l%i==0:
            return False
    return True

def obciecie(n, i, j):
 
    dl = int(log10(n))+1
    nowa = (n%(10**(dl-i)))//(10**j)
    return nowa

def solve(n):

    maksi = 0
    dl = int(log10(n))+1
    for i in range(dl-1): #uciecie z lewej
        for j in range(dl-1-i): #uciecie z prawej
            if pierwsza(obciecie(n, i, j)):
                maksi = max(maksi, obciecie(n, i, j))
    return maksi


if __name__=="__main__":

    n = 1111 #4
    
    print(solve(n))


