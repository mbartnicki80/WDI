from random import randint

def sum(tab, pocz):

    sumawar = tab[0]
    sumaind = pocz

    for i in range(1, len(tab)):
        if tab[i]>tab[i-1]:
            sumawar += tab[i]
            sumaind = pocz+i

    if sumaind==sumawar:
        return len(tab)
    else:
        return 0
        

    


def dlugosc(tab):

    maxsuma = 0

    for i in range(len(tab)):
        for j in range(i, len(tab)):
            maxsuma = max(sum(tab[i:j+1], i), maxsuma)
            
    return maxsuma


if __name__=="__main__":

    #n = int(input("Podaj n:"))
    tab=[2,1,2,3,1,2]
    #tab = [randint(0,1) for i in range(n)]
    print(tab)

    print(dlugosc(tab))