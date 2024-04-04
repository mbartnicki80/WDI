from msvcrt import kbhit


def czy(a, b):

    for i in range (2, 17):
        znaleziona = 0
        k = a
        l = b
        tab = [0]*16

        while k>0:
            tab[k%i] = 1
            k //= i
        
        while l>0:
            if tab[l%i] == 1:
                znaleziona = 1
                break
            l //= i

        if znaleziona == 0:
            return i

    return "Nie ma"

if __name__=="__main__":

    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))

    print(czy(a, b))