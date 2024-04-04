def solve(tab, waga, sumwag, ind, t):

    if ind==len(tab):
        if sumwag==waga:
            for i in range(len(t)):
                print(t[i])
            return True
        else: return False
        
    return solve(tab, waga, sumwag+tab[ind], ind+1, t+[tab[ind]]) or solve(tab, waga, sumwag, ind+1, t) or solve(tab, waga+tab[ind], sumwag, ind+1, t+[tab[ind]])

if __name__=="__main__":

    tab = [2, 5]; t=[]
    waga = 7

    print(solve(tab, waga, 0, 0, t))