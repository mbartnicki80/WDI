if __name__=="__main__":

    n = int(input("Podaj n:"))

    for i in range(10**(n-1), (10**n)-1):
        a = i
        suma = 0
        while a!=0:
            suma += (a%10)**n
            a //= 10

        if suma==i:
            print(i)
