from math import log10


def palindrom(n):

    a = n
    nowa = 0

    while a>0:
        nowa *= 10
        nowa += a%10
        a //= 10
    
    if nowa == n:
        return 1
    return 0

def palindrom2(n):

    a = n
    nowa = 0

    while a>0:
        nowa *= 2
        nowa += a%2
        a //= 2

    nowa1 = 0
    dl = int(log10(nowa)+1)
    a = nowa

    while a>0:
        nowa1 *= 2
        nowa1 += a%2
        a //= 2

    if nowa == nowa1:
        return 1
    return 0

if __name__=="__main__":

    n = int(input("Podaj liczbę: "))
    
    if palindrom(n) == 0:
        print("NIE PALINDROM")
    else:
        print("TAK PALINDROM")
    
    if palindrom2(n) == 0:
        print("NIE PALINDROM2")
    else:
        print("TAK PALINDROM2")