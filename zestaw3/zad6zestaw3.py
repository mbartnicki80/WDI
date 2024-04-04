from random import randint


if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [randint(1, 1000) for _ in range(n)]
    print(tab)
    
    for i in range(n):
        a = tab[i]
        znaleziono = 0

        while a>0:
            if a%2==1:
                znaleziono = 1
                break
            a //= 10

        if znaleziono == 0:
            print("NIE")
            break
        
    else:
        print("TAK")