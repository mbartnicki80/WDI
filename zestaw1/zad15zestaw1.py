import math
if __name__=="__main__":
    eps=float(input("Podaj przybliżenie:"))
    wpi=math.sqrt(0.5)
    wartosc=math.sqrt(0.5)
    while(abs(1-wpi)>eps):
        wpi=math.sqrt(1/2*wpi+1/2)
        print(wpi)
        wartosc*=wpi
    pozycja=-1
    tmp=eps**(-1)
    while (tmp>0):
        tmp//=10
        pozycja+=1
    print(round(2/wartosc,pozycja))