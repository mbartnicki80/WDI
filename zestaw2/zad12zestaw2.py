from math import log10


if __name__=="__main__":

    n = int(input("Podaj liczbę: "))
    dl = int(log10(n)+1)

    for i in range (0, dl):
        if (n//(10**i))%10==dl:
            print("TAK")
            exit()
    
    print("NIE")