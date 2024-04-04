def cyfra(ele):

    while ele>0:
        if ele%10 == 2 or ele%10 == 5 or ele%10 == 7 or ele%10 == 3:
            return 1
        ele //= 10

    return 0
    


def funk(tab, n):

    for i in range(n):
        for j in range(n):
            if cyfra(tab[i][j])==0:
                break
        else: 
            return True

    return False

                
if __name__=="__main__":

    n = int(input("Podaj n: "))
    tab = [[3,2,1],[4,2,1],[4,2,1]]

    print(funk(tab, n))