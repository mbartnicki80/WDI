def solve(tab, sumele, sumind, ind, l):

    if ind==len(tab):
        if sumele==sumind and l>0: 
            return l, sumele
        return(len(tab), 0)


    return min(solve(tab, sumele+tab[ind], sumind+ind, ind+1, l+1), solve(tab, sumele, sumind, ind+1, l))

if __name__=="__main__":

    tab = [1, 7, 3, 5, 11, 2]
    print(solve(tab, 0, 0, 0, 0))