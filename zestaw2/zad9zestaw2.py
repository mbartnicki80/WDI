def prostokat(odl, prawa):
    
    wysokosc=1/prawa
    return odl*wysokosc

if __name__=="__main__":

    k = int(input("Podaj granicę przedziału: "))
    n = int(input("Podaj liczbę prostokątów: "))

    odl = (k-1)/n
    suma = 0
    
    for i in range(1,n):
        suma+=prostokat(odl, 1+odl*i)

    print(suma)