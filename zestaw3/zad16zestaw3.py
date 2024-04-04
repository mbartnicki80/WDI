from random import randint

def czyjedyna(tab, n):

    najm = 101
    najw = -1

    for i in range(n):
        najw = max(najw, tab[i])
        najm = min(najm, tab[i])

    licz= 0
    for i in range(n):
        if tab[i]==najw or tab[i]==najm:
            licz += 1
            if licz>1:
                return 0

    return 1

if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [randint(0,100) for _ in range(n)]
    print(tab)
    print(czyjedyna(tab, n))