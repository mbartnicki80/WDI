def an(i):
    return i*i+i+1

if __name__=="__main__":

    n = int(input("Podaj liczbę: "))
    i = 1

    while (an(i)<=n):
        if n%an(i)==0:
            print("TAK")
            exit()
        i+=1
        
    print ("NIE")