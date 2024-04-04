def samogl(s1, s2):

    suma1 = 0
    suma2 = 0

    for i in s1:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y':
            suma1 += 1
    for i in s2:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y':
            suma2 += 1

    if suma1==suma2:
        return True
    return False

def waga(s1, s2):

    suma1 = 0
    suma2 = 0

    for i in s1:
        suma1 += ord(i)
    for i in s2:
        suma2 += ord(i)

    if suma1==suma2:
        return True
    return False


def wyraz(s1, s2):

    def solve(s1, s2, tab, ind):
        
        if ind==len(tab):
            if waga(s1, s2) and samogl(s2, s2):
                print(s2)
                return
            else:
                return False
        
        solve(s1, s2, tab, ind+1)
        solve(s1, s2+[tab[ind]], tab, ind+1)

    tab = list(s2)
    solve(s1, [], tab, 0)


if __name__=="__main__":

    s1 = input(); s2 = input()
    wyraz(s1, s2)