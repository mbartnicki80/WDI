from math import sqrt


def czypierwsza(l):

    if l==0 or l==1:
        return 0

    for i in range(2, int(sqrt(l)+1)):
        if l%i==0:
            return 0
    return 1

def bin(liczba):

    nowa = 0
    pot = 0
    while liczba>0:
        nowa += (liczba%2)*(2**pot)
        pot += 1
        liczba //= 10
    return nowa

def solve(a, b, liczba):

    if a==0 and b==0:
        if czypierwsza(bin(liczba))==0:
            return 1
        return 0

    suma = 0
    if a>0:
        suma += solve(a-1, b, liczba*10+1)
    if b>0:
        suma += solve(a, b-1, liczba*10)
    
    return suma

if __name__=="__main__":

    a = int(input()); b = int(input())
    print(solve(a-1, b, 1))