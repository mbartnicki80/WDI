def nwd(a,b):
    if (b<a):
        a,b=b,a
    while(b!=0):
        a,b=b,a%b
    return a

if __name__=="__main__":
    print("Podaj a:")
    a=int(input())
    print("Podaj b:")
    b=int(input())
    print("Podaj c:")
    c=int(input())
    nww1=a*b/nwd(a,b)
    print("NWW:",int(nww1*c/nwd(nww1,c)))