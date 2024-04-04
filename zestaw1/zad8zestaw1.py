if __name__ == "__main__":
    liczba=int(input("Podaj liczbę:"))
    for i in range (2, int(liczba**(1/2))+1):
        if liczba%i==0:
            print("Nie jest")
            exit()
    print("Jest")