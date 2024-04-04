if __name__=="__main__":
    eps=float(input("Podaj epsilon:"))
    a,b=1,10
    while (abs(a-b)>eps):
        sr=(a+b)/2
        if (sr**sr>2020):
            b=sr
        else:
            a=sr
    pozycja=-1
    tmp=eps**(-1)
    while (tmp>0):
        tmp//=10
        pozycja+=1
    print(round(a,pozycja))