from math import log10, sqrt

def sumacyfr(a):

    dl = int(log10(a)+1)
    suma = 0
    for j in range(0, dl):
            suma += (a//(10**j))%10

    return suma

if __name__=="__main__":

    for i in range(2, 1000001):
        a = i
        sumadzielnik = 0
        sumaliczby = sumacyfr(a)
        dzielnik = 2

        while a>1 and dzielnik<=int(sqrt(a))+1:
            if a%dzielnik == 0:
                sumadzielnik += sumacyfr(dzielnik)
                a //= dzielnik
            else:
                dzielnik += 1

        if sumadzielnik == 0:
            continue

        if a>1:
            sumadzielnik += sumacyfr(a)
        
        if sumaliczby == sumadzielnik:
            print(i)