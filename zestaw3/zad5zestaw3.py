if __name__=="__main__":

    tab = [0 for i in range(1000)]

    iter = 0
    while True:
        n = int(input("Podaj n: "))
        if n == 0:
            break
        tab[iter] = n
        iter += 1

    for i in range(10):
        mini = tab[i]
        ind = i
        for j in range(i+1, iter):
            if tab[j]<mini:
                ind = j
                
        tab[i], tab[ind] = tab[ind], tab[i]
    
    print(tab[9])