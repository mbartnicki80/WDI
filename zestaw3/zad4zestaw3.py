if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [0 for i in range(n)]

    print(2, end='')
    print('.', end='')

    silnia = 1
    ind = 1
    for i in range(n):
        ind += 1
        silnia *= ind

        ulam = 1
        l = 10
        while ulam<n:
            tab[ulam] += l//silnia
            if tab[ulam]>=10:
                ulam2 = ulam
                while ulam2>0 and tab[ulam2]>=10:
                    tab[ulam2], tab[ulam2-1] = tab[ulam2]%10, tab[ulam2-1]+tab[ulam2]//10
                    ulam2 -= 1
            l = (l%silnia)*10
            ulam += 1
        
    for i in range(2, 1000):
        print(tab[i], end='')
    
