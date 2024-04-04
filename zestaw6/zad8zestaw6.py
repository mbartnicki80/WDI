def solve(tab, waga, sumwag, ind):

    if ind==len(tab):
        if sumwag==waga:
            return True
        return False
        
    return solve(tab, waga, sumwag+tab[ind], ind+1) or solve(tab, waga, sumwag, ind+1) or solve(tab, waga+tab[ind], sumwag, ind+1)

if __name__=="__main__":

    tab = [1, 5]
    waga = 2
    print(solve(tab, waga, 0, 0))