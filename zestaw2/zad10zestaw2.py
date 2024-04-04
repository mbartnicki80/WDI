def an(a):
    return 3*a+1

if __name__=="__main__":

    n = int(input("Podaj liczbę: "))
    a = 2

    while a<=n:
        if n%a==0:
            print("Tak")
            exit()
        a = an(a)
    
    print("Nie")