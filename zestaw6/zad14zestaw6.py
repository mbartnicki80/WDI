def hanoi(n, z, na, posrednik):

    if n==0:
        return
    
    hanoi(n-1, z, posrednik, na)
    print(f"Klocek {n} na {na} z {z}")
    hanoi(n-1, posrednik, na, z)

if __name__=="__main__":

    n = int(input())
    hanoi(n, "A", "B", "C")