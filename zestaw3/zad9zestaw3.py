def podciag(tab):

    suma = 1
    maxsuma = 1

    for i in range(1, n):
        if tab[i]>tab[i-1]:
            suma += 1
            maxsuma = max(maxsuma, suma)
        else:
            suma = 1
    
    return maxsuma

if __name__=="__main__":

    n = int(input("Podaj n:"))
    tab = [int(input()) for i in range(n)]
    print(podciag(tab))

    