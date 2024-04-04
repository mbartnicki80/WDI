def podzielniki(liczba, t):

    dzielnik = 2
    i = 0

    while liczba>1:
        if liczba%dzielnik==0:
            t[i]=dzielnik
            i += 1
            while liczba%dzielnik==0:
                liczba //= dzielnik
        dzielnik += 1
    
    return t

def solve(t, ind, dl, t1):

    if ind==dl:
        if len(t1)>0:
            iloczyn = 1
            for i in t1:
                iloczyn *= i
            return iloczyn
        return False

    suma = 0
    suma += solve(t, ind+1, dl, t1+[t[ind]])
    suma += solve(t, ind+1, dl, t1)

    return suma

if __name__=="__main__":

    t = [0 for i in range(20)]
    suma = 0
    podzielniki(60, t)
    for i in range(20):
        if t[i]==0:
            break
        suma += 1

    print(solve(t, 0, suma, []))