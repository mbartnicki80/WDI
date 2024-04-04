def czynniki(liczba):

    czynnik = 2
    suma = 0
    while liczba>1:
        if liczba%czynnik==0:
            suma += 1
            while liczba%czynnik==0:
                liczba //= czynnik
            if suma>2:
                return False
        czynnik += 1

    if suma == 2:
        return True
    return False

def square(T):

    n = len(T)
    for i in range(n):  
        for j in range(n): #lewy gorny wierzcholek
            for k in range(1, min(n-j, n-i)): #dlugosc
                if czynniki(T[i][j]*T[i+k][j+k]*T[i][j+k]*T[i+k][j]):
                    return True
    
    return False

if __name__=="__main__":

    tab = [[1,2,3],[1,2,3],[1,2,3]] #ma dac tak
    print(square(tab))