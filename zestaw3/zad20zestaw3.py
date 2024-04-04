from random import randint

def sum(tab):

    iloczyn = 1

    for i in range(len(tab)):
        iloczyn *= tab[i]

    dzielnik = 2
    while iloczyn>1:
        j = 0
        while iloczyn%dzielnik==0:
            j += 1
            iloczyn //= dzielnik
            if j>1:
                return 0
        dzielnik +=1

    return len(tab)
        

    


def dlugosc(tab):

    maxsuma = 0

    for i in range(len(tab)):
        for j in range(i, len(tab)):
            maxsuma = max(sum(tab[i:j+1]), maxsuma)
            
    return maxsuma


if __name__=="__main__":

    #n = int(input("Podaj n:"))
    tab=[2,23,33,35,7,4,6,7,5,11,13,22]
    #tab = [randint(0,1) for i in range(n)]
    print(tab)

    print(dlugosc(tab))