def fib(i):

    suma = 1
    a1 = 1
    a2 = 1
    b1 = 1
    b2 = 1
    while a2<=i and suma!=i:
        while suma<i:
            suma+=a2
            a1, a2 = a2, a1+a2
        while suma>i:
            suma-=b1
            b1, b2 = b2, b1+b2
    
    if suma==i:
        return 1
    return 0

if __name__=="__main__":

    n = int(input("Podaj liczbę: "))

    while(True):
        if fib(n+1)==0:
            print(n+1)
            exit()
        n+=1
    
