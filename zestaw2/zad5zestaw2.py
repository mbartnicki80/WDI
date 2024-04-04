from math import log10


def bin(n):
    
    i = 0
    binarka = 0

    while n>0:
        binarka+=(n%2)*(10**i)
        i+=1
        n//=2

    return binarka

if __name__=="__main__":

    n = int(input("Podaj liczbę: "))
    podz = int(input("Podaj podzielność: "))
    dl = int(log10(n)+1)
    licznik = 0

    for i in range(1, 2**dl):
        a = bin(i)
        liczba = 0
        dlliczby = 0

        for j in range(dl):
            if (a//(10**j))%10==1:
                liczba+=(n//(10**j))%10*(10**dlliczby)
                dlliczby+=1

        if (liczba%podz==0):
            licznik+=1

    print(licznik)