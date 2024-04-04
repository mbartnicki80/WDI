if __name__=="__main__":

    a = int(input("Podaj a: "))
    b = int(input("Podaj a: "))
    n = int(input("Podaj a: "))

    print(a//b, end="")
    print(".", end="")

    while n>0:
        a = (a%b)*10
        if (a==0):
            break
        print(a//b, end="")
        n-=1