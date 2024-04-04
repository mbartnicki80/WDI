from math import log10

def rek(x, y, n, p=0):

    if x==y:
        return 1
    if n==0 or x==y:
        if x==y:
            return 1
        else:
            return 0
    
    dl = int(log10(x))+1
    suma = 0
    if p!=1:
        suma += rek(x+3, y, n-1, 1)
    if p!=2:
        suma += rek(x*2, y, n-1, 2)
    if p!=3:
        for i in range(dl):
            if (x//(10**i))%2==0:
                x += 10**i
        suma += rek(x, y, n-1, 3)


    return suma

if __name__=="__main__":
    print(rek(11, 31, 4))
    