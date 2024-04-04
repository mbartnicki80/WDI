import math
if __name__=="__main__":
    a=int(input("Podaj pierwszą liczbę: "))
    b=int(input("Podaj pierwszą liczbę: "))
    while (abs(a-b)>0.000000001):
        a,b=math.sqrt(a*b),(a+b)/2.0
    print(a)