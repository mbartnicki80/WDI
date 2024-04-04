def solve(tab, szukana, suma, ind):

    if ind==len(tab):
        if suma==szukana:
            return True
        return False
    
    return solve(tab, szukana, suma+tab[ind], ind+1) or solve(tab, szukana, suma, ind+1)


if __name__=="__main__":

    szukana = int(input())
    tab =[15,1,3,6,2,1]
    print(solve(tab, szukana, 0, 0))
