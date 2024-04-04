from random import randint

def czypal(slice):

    i = 0
    j = len(slice)-1
    suma = 0

    while i<j:
        if slice[i]!=slice[j] or slice[i]%2==0 or slice[j]%2==0:
            return 0
        suma += 2
        i += 1
        j -= 1
    
    if i==j and slice[j]%2==1:
        suma += 1
    elif i==j:
        return 0

    return suma


def dlugosc(slice):

    maxsuma = 0

    for i in range(len(slice)):
        for j in range(i, len(slice)):
            maxsuma = max(czypal(slice[i:j+1]), maxsuma)
            
    return maxsuma


if __name__=="__main__":

    #n = int(input("Podaj n:"))
    slice = [0,2,3,5,7,7,5,3,6]
    #slice = [randint(0,1) for i in range(n)]
    print(slice)

    print(dlugosc(slice))