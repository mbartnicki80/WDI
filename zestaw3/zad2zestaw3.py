

def czy(a, b):

    taba = [0 for i in range(10)]
    tabb = [0 for i in range(10)]

    while a>0:
        taba[a%10] = 1
        a //= 10
    
    while b>0:
        tabb[b%10] = 1
        b //= 10

    for i in range(10):
        if taba[i]!=tabb[i]:
            return False
    
    return True


if __name__=="__main__":

    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    
    print(czy(a, b))