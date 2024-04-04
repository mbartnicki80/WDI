def szachy(w, tab, hetman, suma):
    n = len(tab)
    if w==n:
        return suma==0

    p = False
    
    for i in range(n):
        if w!=0:
            if hetman==i-1 or hetman==i or hetman==i+1:
                continue
        p |= szachy(w+1, tab, i, suma+tab[w][i])

    return p

if __name__=="__main__":
    tab=[
        [1,2,3,4,5],
        [1,2,1,4,5],
        [1,2,3,4,5],
        [1,2,1,4,5],
        [7,2,3,4,5]
    ]
    print(szachy(0, tab, -5, 0))