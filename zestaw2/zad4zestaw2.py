from math import sqrt


def dwatrzypiec(n):

    while n%2==0:
        n/=2

    while n%3==0:
        n/=3
    
    while n%5==0:
        n/=5

    if n==1:
        return 1
    
    return 0

if __name__=="__main__":

    n = int(input("Podaj zakres: "))
    suma = 1

    for i in range(2, n+1):
        suma += dwatrzypiec(i)
    
    print(suma)
