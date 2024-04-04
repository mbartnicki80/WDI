from math import log10

if __name__=="__main__":

    n = int(input("Wprowadź liczbę: "))
    dl = int(log10(n))
    potega = dl
    prev = -1

    for i in range(dl, -1, -1):
        if (n//(10**potega))%10<=prev:
            print("NIE")
            exit()
        prev = (n//(10**potega))%10
        potega -= 1

    print ("TAK")