def solve(tab):

    n = len(tab)
    for i in range(n):
        for j in range(i+1, n):
            if not (tab[i][0]<=tab[j][0]<=tab[i][1] or tab[i][0]<=tab[j][1]<=tab[i][1]):
                if (tab[i][1]-tab[i][0])+(tab[j][1]-tab[j][0])==2022:
                    return True
    return False


if __name__=="__main__":
    tab = [(1, 2021), (2020, 2022)]
    print(solve(tab))