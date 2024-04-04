from random import randint


if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [randint(1, 1000) for _ in range(n)]
    print(tab)
    
    for i in range(n):
        a = tab[i]
        znaleziono = 0

        while a>0:
            if a%2==0:
                break
            a //= 10

        if a == 0:
            print("TAK")
            break     
         
    else:
        print("NIE")