from math import log10, sqrt

def pierwsze(n):

    if n==1 or n==0:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n%i==0:
            return False
    return True

def rek(n, kawalki):

    if n==0 and pierwsze(kawalki):
        return True
    elif n==0:
        return False

    dl = int(log10(n)+1)
    w = False
    for i in range(1, dl+1):
        if pierwsze(n//(10**(dl-i))):
            w |= rek(n%(10**(dl-i)), kawalki+1)
    return w

def divide(n):

    dl = int(log10(n)+1)
    w = False
    for i in range(1, dl+1):
        if pierwsze(n//(10**(dl-i))):
            w |= rek(n%(10**(dl-i)), 1)
    return w

if __name__=="__main__":
    n = int(input())
    print(divide(n))