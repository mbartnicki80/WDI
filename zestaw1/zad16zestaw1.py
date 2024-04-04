def ciag(num):
    return (num%2)*(3*num+1)+(1-num%2)*num/2

if __name__=="__main__":
    maxkrok=0
    maxi=0
    for i in range (2,10001):
        num=i
        j=0
        while (abs(1-num)>0.000001):
            num=ciag(num)
            j+=1
        if j>maxkrok:
            maxkrok=j
            maxi=i
    print(maxi)