def fibonacci(f0,f1):
    fib=0
    while (f0+f1<2022):
        fib=f0+f1
        f0=f1; f1=fib
    if (f0+f1==2022):
        return True
    else:
        return False
        

if __name__ == "__main__":
    f0=1; f1=1
    najsuma=2022
    f0min=0; f1min=0
    for i in range (1,2022):
        f0=i
        for j in range (1, 2022-i+1):
            f1=j
            if (fibonacci(f0, f1)==True):
                if (f0+f1<najsuma):
                    najsuma=f0+f1
                    f0min=f0; f1min=f1
    print (f0min,f1min)