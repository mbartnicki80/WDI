def zamiana(n, i):

    tab = [0 for _ in range(1000)]
    j = 0
    while n>0:
        tab[j] = n%i
        n //= i
        j += 1

    print(i, end=" ")
    while j-1>=0:
        print(tab[j-1] if tab[j-1]<10 else chr(tab[j-1]-10+ord('A')), end="")
        j -= 1
    
    print()



if __name__=="__main__":

    n = int(input("Podaj liczbę: "))

    for i in range(2, 17):
        zamiana(n, i)