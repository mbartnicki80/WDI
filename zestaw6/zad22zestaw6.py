def solve(tab, i, suma):

    if i==len(tab)-1:
        return suma

    w = 0
    dzielnik=2
    k=tab[i]
    sum = 0
    
    while k>1:
        if k%dzielnik==0:
            if dzielnik!=tab[i] and i+dzielnik<len(tab):
                sum += solve(tab, i+dzielnik, suma+1)
            while k%dzielnik==0:
                k//=dzielnik
        dzielnik += 1
    
    return sum

if __name__=="__main__":

    tab =[6,1,6,1,2,1]
    print(solve(tab, 0, 0))