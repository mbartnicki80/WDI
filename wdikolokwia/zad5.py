from math import sqrt

def solve(tab, n):

    dlugosc1 = 1
    min1 = 0
    min2 = 0
    max1 = 0
    max2 = 0
    for i in range(1, n):

        if tab[i]>tab[i-1]:
            if dlugosc1==1:
                min1 = tab[i-1]
            dlugosc1 += 1
        elif dlugosc1>2:
            max1 = tab[i-1]
            j = i
            dlugosc2 = 1
            while j<n:
                if tab[j]>tab[j-1]:
                    if dlugosc2 == 1:
                        min2 = tab[j-1]
                    dlugosc2 += 1 
                elif dlugosc2>2:
                    max2 = tab[j-1]
                    if max2<min1 or max2<min1:
                        return True
                    dlugosc2 = 1 
                else:
                    dlugosc2 = 1
                j += 1
            dlugosc1 = 1
        else:
            dlugosc1 = 1
                
    return False

if __name__=="__main__":

    t = [2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2] 
    
    print(solve(t, len(t)))