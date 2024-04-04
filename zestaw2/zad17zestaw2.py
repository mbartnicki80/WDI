from math import e, log, log10

def f(x):
    return x**x-2020

def df(x):
    return x**x*(1+log(x))

if __name__=="__main__":

    eps = 0.001
    x = 3
    h = -f(x)/df(x)
    while abs(h)>eps:
        h = -f(x)/df(x)
        x += h
        
    print(round(x, int(-log10(eps))))

