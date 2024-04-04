if __name__=="__main__":
    x=float(input("Podaj wartość x:"))
    eps=float(input("Podaj przybliżenie:"))
    cosx=1
    i=2
    silnia=1/2
    potega=x
    x*=potega
    while(silnia*x>eps):
        if (i%4==0):
            cosx+=(silnia*x)
        elif (i%2==0):
            cosx-=(silnia*x)
        x*=potega
        i+=1
        silnia/=i
        print(cosx)
            

    pozycja=-1
    tmp=eps**(-1)
    while (tmp>0):
        tmp//=10
        pozycja+=1
    print(round(cosx,pozycja))