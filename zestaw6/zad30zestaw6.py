from math import sqrt

def srodek(t):

    suma1 = 0
    suma2 = 0
    for i in t:
        suma1 += i[0]
        suma2 += i[1]
    return suma1/len(t), suma2/len(t)


def solve(t, r, k):

    def reku(t, t1, ind, r):

        if ind==len(t):
            if len(t1)%3==0 and len(t1)<k and len(t1)>0:
                d = srodek(t1)
                if sqrt(d[0]**2+d[1]**2)<r:
                    return True
            return False
        
        return reku(t, t1, ind+1, r) or reku(t, t1+[(t[ind])], ind+1, r)
    
    print(reku(t, [], 0, r))

if __name__=="__main__":

    r = int(input()); k = int(input())
    t = [(1,1),(1,2),(1,2)] #true
    #r = 1; k = 4
    solve(t,r,k)
    