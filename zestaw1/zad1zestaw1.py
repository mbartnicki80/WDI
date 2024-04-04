if __name__ == "__main__":
    f0=0; f1=1
    print(f0)
    print(f1)
    while (f0+f1<1000000):
        fib=f0+f1
        f0=f1; f1=fib
        print(fib)
