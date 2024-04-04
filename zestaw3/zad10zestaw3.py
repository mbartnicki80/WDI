def podciagar(tab):

    r = tab[1]-tab[0]
    suma = 1
    maxsuma = 1

    for i in range(2, n):
        if tab[i]-tab[i-1]!=r:
            suma = 1
            r = tab[i]-tab[i-1]
        else:
            suma += 1
            maxsuma = max(maxsuma, suma)
    
    return maxsuma

if __name__=="__main__":

    n = int(input("Podaj n:"))
    tab = [int(input()) for i in range(n)]
    print(podciagar(tab))

    