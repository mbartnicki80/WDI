if __name__ == "__main__":
    liczba=int(input("Podaj liczbę:"))
    for i in range (1, int(liczba**(1/2))):
        if liczba%i==0:
            print(i, int(liczba/i), end=" ")
    if (int(liczba**(1/2))**2==liczba):
        print(int(liczba**(1/2)))