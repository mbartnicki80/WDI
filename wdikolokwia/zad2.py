from math import sqrt


def czypierwsza(liczba):

    for i in range(2, int(sqrt(liczba))+1):
        if liczba%i==0:
            return False
    return True

def solve(t, n):

    iloczyn = 1
    maksi = 0
    for i in range(n):
        if t[i]==iloczyn:
            maksi = max(maksi, t[i])
        if czypierwsza(t[i]):
            iloczyn *= t[i]

    if maksi==0:
        return None
    return maksi



if __name__=="__main__":

    t = [2,15,17,34,13,442,1,1,1,2] 
    
    print(solve(t, len(t)))


