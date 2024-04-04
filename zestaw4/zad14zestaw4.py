def dwojka(ele):

    suma = 0
    while ele>0:
        if ele%2==1:
            suma += 1
        ele //= 2
    
    return suma


def funk(tab1, tab2, n1, n2):

    for i in range(n1-n2+1):
        for j in range(n1-n2+1):
            sumazg = 0
            for k in range(n2):
                for l in range(n2):
                    if dwojka(tab1[k+i][l+j])==dwojka(tab2[k][l]):
                        sumazg += 1
            if sumazg/(n2**2)>0.33:
                return True

    return False

                
if __name__=="__main__":

    n1 = int(input("Podaj n1: "))
    n2 = int(input("Podaj n2: "))
    tab1 = [[4,2,1],[4,2,1],[4,2,1]]
    tab2 = [[3,3,3],[3,3,3],[1,1,1]]

    print(funk(tab1, tab2, n1, n2))