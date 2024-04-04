from math import log10

if __name__=="__main__":

    n = int(input("Podaj liczbę: "))
    dl = int(log10(n)+1)
    ostatnia = n%10

    for i in range(1,dl):
        if (n//10**i)%10==ostatnia:
            print("NIE")
            exit()

    print("TAK")