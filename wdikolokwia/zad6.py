from math import sqrt

def solve(tab, n):

    maksi = 0
    for i in range(n): #ktory napis
        for dl in range(1, len(tab[i])//2+1): #dlugosc napisu
            for j in range(len(tab[i])): #poczatek napisu
                if j+(dl*2)-1<len(tab[i]):
                    print(tab[i][j:j+dl], tab[i][j+dl:j+(dl*2)])
                    if tab[i][j:j+dl] == tab[i][j+dl:(j+dl)*2] :
                        maksi = max(maksi, len(tab[i][j:j+dl]))
    return maksi
        
if __name__=="__main__":

    t = ["ABCABC", "ABAB", "AA"] 
    
    print(solve(t, len(t)))