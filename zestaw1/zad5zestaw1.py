if __name__ == "__main__":
    szukana=float(input("Podaj pierwiastek:"))
    eps=float(input("Podaj przybliżenie:"))
    a,b=szukana,1
    while (abs(a-b)>eps):
        a=(a+b)/2
        b=szukana/a
    pozycja=-1
    tmp=eps**(-1)
    while (tmp>0):
        tmp//=10
        pozycja+=1
    print(round(a,pozycja))
