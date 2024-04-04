from random import randint


if __name__=="__main__":

    for i in range(20, 41):
        suma = 0
        for j in range(10000):
            tab = [0 for _ in range(365)]

            for k in range(20):
                tab[randint(0, 364)] += 1

            for k in tab:
                if tab[k]>1:
                    suma += 1
        print(i, suma/10000)
