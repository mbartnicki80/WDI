from math import sqrt


if __name__=="__main__":

    n = int(input("Podaj liczbę: "))
    
    for i in range(int(sqrt(n)), 0, -1):
        if n%i==0:
            print(i, "*", int(n/i))
            exit()
    