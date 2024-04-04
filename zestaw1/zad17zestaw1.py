if __name__=="__main__":
    n=int(input("Podaj ilość sprawdzanych par: "))
    for i in range (n):
        a=int(input("Podaj pierwszą liczbę: "))
        b=int(input("Podaj drugą liczbę: "))
        iloraz=0
        n=max(a,b)
        m=min(a,b)
        while (abs(iloraz-n/m)>0.00000001):
            iloraz=n/m
            m, n = n, n+m
        print("Iloraz:",iloraz)