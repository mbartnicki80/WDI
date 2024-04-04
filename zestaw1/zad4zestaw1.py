if __name__ == "__main__":
    suma=0
    licznik=0
    s0,r=1,2
    szukana=int(input("Proszę podać liczbę:"))
    while (suma<szukana):
        suma+=s0
        s0+=r
        licznik+=1
    print(licznik)