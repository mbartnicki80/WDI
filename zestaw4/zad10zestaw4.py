def funk(tab, n):

    for i in range(n):
        for j in range(n):
            if tab[i][j]==0:
                break
        else:
            return 0

    for j in range(n):
        for i in range(n):
            if tab[i][j]==0:
                break
        else:
            return False
            
    return True


if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [[0,2,2,2,1],[1,0,3,2,2],[1,2,0,4,2],[1,2,3,0,5],[1,2,3,4,0]]

    for i in range(n):
        for j in range(n):
            print(tab[i][j], end=" ")
        print('')

    print(funk(tab, n))