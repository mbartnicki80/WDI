def an(a1, b0, a0):

    return a1-b0*a0

def bn(b0, a1):

    return b0+2*a1


if __name__=="__main__":

    a0 = 0; a1 = 1
    b0 = 2

    while True:
        n = int(input("Podaj liczbę:"))

        if n == an(a1, b0, a0):
            print(bn(b0, a1))
            a1, a0, b0 = an(a1, b0, a0), a1, bn(b0, a1)
        else:
            print("Nie należy do ciągu")
            exit()