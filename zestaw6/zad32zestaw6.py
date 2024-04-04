def sumaele(t):

    suma = 0
    for i in t:
        suma += i
    
    return suma

def solve(t, k):

    def reku(t, k, t1, t2, ind):

        if ind==len(t):
            if len(t1)>0 and len(t2)>0 and sumaele(t1)==sumaele(t2) and len(t1)+len(t2)==k:
                return True
            return False

        
        return reku(t, k, t1+[t[ind]], t2, ind+1) or reku(t, k, t1, t2+[t[ind]], ind+1) or reku(t, k, t1, t2, ind+1)

    print(reku(t, k, [], [], 0))

if __name__=="__main__":

    k=4
    t = [1,1,1,1]

    solve(t, k)