from math import log10, sqrt


def pierwsza(n):

    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

def wykresl(liczba):

    dl = int(log10(liczba))+1
    if pierwsza(liczba)==1:
        print(liczba)

    if dl==2:
        return False
    
    for i in range(dl):
        wykresl(int((liczba//(10**(dl-i))*(10**(dl-i-1)))+(liczba%(10**(dl-1-i)))))
    

if __name__=="__main__":

    n = int(input("Podaj n:"))
    wykresl(n)
