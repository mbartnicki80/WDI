if __name__=="__main__":
    szukana=int(input("Podaj liczbę:"))
    f0,f1=1,1
    while (f0*f1<szukana):
        f0,f1=f1,f0+f1
    if (f0*f1==szukana):
        print("Jest iloczynem")
    else:
        print("Nie jest iloczynem")