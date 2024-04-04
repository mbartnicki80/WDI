def ilejed(t):

    suma = 0
    for i in t:
        while i>0:
            suma += i%2
            i //= 2
    return suma


def solve(t, t1, t2, t3, ind):
    
    if ind==len(t):
        if len(t1)>0 and len(t2)>0 and len(t3)>0 and ilejed(t1)==ilejed(t2)==ilejed(t3):
            return True
        return False
    
    return solve(t, t1+[t[ind]], t2, t3, ind+1) or solve(t, t1, t2+[t[ind]], t3, ind+1) or solve(t, t1, t2, t3+[t[ind]], ind+1) or solve(t, t1, t2, t3, ind+1)

if __name__=="__main__":

    t = [2,3,5,7,15] #true
    #t = [5,7,15] #falsch
    print(solve(t, [], [], [], 0))
