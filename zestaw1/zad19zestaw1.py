if __name__=="__main__":
    eps=float(input("Podaj przybliżenie:"))
    euler=2
    eulerp=0
    silnia=1
    i=2
    while(abs(euler-eulerp)>eps):
        eulerp=euler
        silnia/=i
        euler+=silnia
        i+=1
        print(euler)

    pozycja=-1
    tmp=eps**(-1)
    while (tmp>0):
        tmp//=10
        pozycja+=1
    print(round(euler,pozycja))