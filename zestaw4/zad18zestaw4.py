def funk(tab, n):

    maxsuma = 0

    for i in range(n):
        for j in range(n):
            a = j
            sumele = 1
            suma = 0

            while a<n and sumele <= 10:
                suma += tab[i][a]
                a += 1
                sumele += 1
                maxsuma = max(suma, maxsuma)
            
    for i in range(n):
        for j in range(n):
            a = j
            sumele = 1
            suma = 0

            while a<n and sumele <= 10:
                suma += tab[a][i]
                a += 1
                sumele += 1
                maxsuma = max(suma, maxsuma)

    return maxsuma

if __name__=="__main__":

    tab = [[0,0,8],[0,1,1],[2,1,2]]
    print(funk(tab, len(tab)))