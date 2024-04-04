def solve(hetman, i):

    if i==8:
        return 1
    
    w = 0
    for j in range(8):
        for k in range(i):
            if hetman[k]==j or abs(k-i)==abs(hetman[k]-j):
                break
        else:
            hetman[i]=j
            w += solve(hetman, i+1)
            hetman[i]=-1

    return w

if __name__=="__main__":

    hetman = [(-1) for i in range(8)]
    print(solve(hetman, 0))