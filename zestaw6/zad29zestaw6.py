from math import sqrt


def srodek(t):

    suma1 = 0
    suma2 = 0
    suma3 = 0
    for i in t:
        suma1 += i[0]
        suma2 += i[1]
        suma3 += i[2]
    return suma1/len(t), suma2/len(t), suma3/len(t)


def solve(t, r):

    def reku(t, t1, ind, r):

        if ind==len(t):
            if len(t1)>2:
                k = srodek(t1)
                if sqrt(k[0]**2+k[1]**2+k[2]**2)<r:
                    return True
            return False
        
        return reku(t, t1, ind+1, r) or reku(t, t1+[t[ind]], ind+1, r)
    
    print(reku(t, [], 0, r))

if __name__=="__main__":

    r = int(input())
    t = [(1,2,1), (1,2,1), (1,2,1)] #true
    # t = [5,7,15] #falsch
    #r = 5
    solve(t, r)
    