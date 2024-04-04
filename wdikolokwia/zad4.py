def zgodne(l1, l2):

    tab1 = [0 for i in range(4)]

    while l1>0:
        tab1[l1%4]=1
        l1 //= 4
    
    while l2>0:
        if tab1[l2%4]==0:
            return False
        l2 //= 4

    return True

def solve(tab):

    n = len(tab)
    maksi = 1
    for i in range(n):
        dlugosc = 1
        for j in range(i+1, n):
            if zgodne(tab[i], tab[j]):
                dlugosc += 1
        maksi = max(maksi, dlugosc)

    return maksi


if __name__=="__main__":

    tab = [13, 23, 29, 1, 1, 2, 2]
    print(solve(tab))