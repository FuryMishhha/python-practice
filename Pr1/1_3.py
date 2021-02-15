import math

def zad1_3(n,m):
    sum1=sum2=0
    for i in range (1,n+1):
        for j in range (1,m+1):
            sum1+=89*j**4+2*j**3+68
    for i in range (1,n+1):
        sum2+=i-math.exp(i)
    return 23*sum1-sum2

print("Задание 1_3",zad1_3(51,76), zad1_3(91,61), sep='\n')
