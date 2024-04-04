if __name__ == "__main__":
    for i in range (2,1000001):
        suma=1
        for j in range (2, int(i**(1/2))):
            if i%j==0:
                suma+=j+i/j
        if int(i**(1/2))**2==i:
            suma+=i**(1/2)
        if suma==i:
            print(i)