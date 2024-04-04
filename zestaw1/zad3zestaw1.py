if __name__ == "__main__":
    szukana=int(input("Podaj sumę:"))
    a1,a2=0,1
    b1,b2=0,1
    suma=0
    while a2<szukana and suma<szukana:
        suma+=a2
        while suma>szukana:
            suma-=b2
            b1,b2=b2,b1+b2
        a1,a2=a2,a1+a2
    if (suma==szukana):
        print("Istnieje")
    else:
        print("Nie istnieje")