from math import sqrt


def czypierwsza(pierwsza, n):

    pierwsza[0] = pierwsza[1] = 0
    for i in range(2, int(sqrt(n))+1):
        if pierwsza[i]==1:
            for j in range(i*i, n, i):
                pierwsza[j] = 0
    
    return pierwsza

def maska(n, t1):

    binarka = [0 for _ in range(len(t1))]
    i = 0
    while n>0:
        binarka[i] = n%3
        n //= 3
        i += 1

    return binarka


def gen(t1, t2):

    pierwsza = [1 for i in range(len(t1)*9+1)]
    czypierwsza(pierwsza, len(t1)*9+1)

 
    for i in range(3**(len(t1))):
        binarka = maska(i, t1)
        suma = 0
        for j in range(len(t1)):
            if binarka[j]==0:
                suma += t1[j]
            elif binarka[j]==1:
                suma += t2[j]
            else:
                suma+= t1[j]+t2[j]
                
        if (pierwsza[suma]) == 1:
            print(suma)

    


if __name__=="__main__":

    t1 = [1,1,1,1]
    t2 = [1,1,1,2]
    gen(t1, t2)