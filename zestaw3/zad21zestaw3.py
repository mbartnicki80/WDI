def nwd(a, b):
    
    if b>a:
        a, b = b, a
    
    while b!=0:
        a, b = b, a%b
    
    return a

def trojki(tab):

    dl = len(tab)
    licznik = 0

    for i in range(dl-2):
        for j in range(1, 3):
            if i+j<dl-1:
                for k in range(1, 3):
                    if i+j+k<dl and nwd(nwd(tab[i], tab[j]), tab[k]) == 1:
                        licznik += 1

    return licznik


if __name__=="__main__":

    tab = [2,1,4]
    
    print(trojki(tab))