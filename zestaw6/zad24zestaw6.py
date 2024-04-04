import math


def sumowanie(t):

    suma1 = 0
    suma2 = 0
    for i in t:
        suma1 += i[0]
        suma2 += i[1]

    return suma1/(len(t)), suma2/(len(t))


def solve(tab, t1, t2, ind):

    if ind==len(tab):
        if len(t1)>1 and len(t2)>1 and t1!=t2:
            k = sumowanie(t1)
            l = sumowanie(t2)
            return math.sqrt((k[0]-l[0])**2+(k[1]-l[1])**2)
        return math.inf


    mini = min(solve(tab, t1+[(tab[ind])], t2, ind+1), solve(tab, t1, t2+[(tab[ind])], ind+1), solve(tab, t1+[(tab[ind])], t2+[(tab[ind])], ind+1), solve(tab, t1, t2, ind+1))

    return mini


if __name__=="__main__":

    tab =[(1,1),(2,2),(2,1)]
    print(solve(tab, [], [], 0))