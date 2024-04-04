from math import log10, sqrt


def czypierwsza(ele):

    for i in range(2, int(sqrt(ele))+1):
        if ele%i==0:
            return 0
    return 1

def solve(a, b, c):

    if a==0 and b==0:
        if czypierwsza(c):
            print(c)
            return 1
        else:
            return False
    
    w = 0
    if a>0:
        w += solve(a%(10**int(log10(a))), b, c*10+a//(10**int(log10(a))))
    if b>0:
        w += solve(a, b%(10**int(log10(b))), c*10+b//(10**int(log10(b))))
    return w

if __name__=="__main__":

    n = int(input())
    m = int(input())

    print(solve(n, m, 0))
