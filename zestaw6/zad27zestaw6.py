def pole(t):

    return (t[1]-t[0])*(t[3]-t[2])


def solve(tab, ile, t):

    if ile==len(tab):
        if len(t)==13:
            suma = 0
            for i in t:
                suma += pole(i)
            if suma==2012:
                return True
        return False
    
    w = 0

    for j in t:
        if (j[0]>=tab[ile][0] and j[0]<=tab[ile][1]) or (j[1]>=tab[ile][0] and j[1]<=tab[ile][1]) or (j[2]>=tab[ile][2] and j[2]<=tab[ile][3]) or (j[3]>=tab[ile][2] and j[3]<=tab[ile][3]):
            break
    else:
        w|=solve(tab, ile+1, t+[(tab[ile])])
        w|=solve(tab, ile+1, t)

    return w




if __name__=="__main__":

    tab=[(1, 1, 1, 1)]
    print(solve(tab, 0, []))
