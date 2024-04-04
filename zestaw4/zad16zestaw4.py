def cyfra(ele):

    while ele>0:
        if ele%10 != 2 or ele%10 != 5 or ele%10 != 7 or ele%10 != 3:
            return 0
        ele //= 10

    return 1
    


def funk(tab, n):

    for i in range(n):
        for j in range(n):
            if cyfra(tab[i][j])==1:
                break
        else: 
            return False

    return True

                
if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [[3,2,1],[4,2,1],[4,2,1]]

    print(funk(tab, n))