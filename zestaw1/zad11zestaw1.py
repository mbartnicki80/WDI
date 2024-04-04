if __name__ == "__main__":
    for i in range (3,1000001):
        suma=1
        suma1=1
        for j in range (2, int(i**(1/2))):
            if i%j==0:
                suma+=j+i/j
        if int(i**(1/2))**2==i:
            suma+=i**(1/2)       
        if suma<=1000000:          #policzenie sumy dzielników 1 liczby
            for j in range (2, int(suma**(1/2))):
                if suma%j==0:
                    suma1+=j+suma/j
            if int(suma**(1/2))**2==suma:
                suma1+=suma**(1/2)
            if suma1<=1000000:     #policzenie sumy dzielników 2 liczby
                if suma1==i and i<suma:
                    print(i, int(suma))