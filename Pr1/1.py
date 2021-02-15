import math

def zad1_1(x,y):
    return (79*x**3-24*y**6)/(y**5+abs(y))+(2*x**8-y**7)/(2*x**7+x**8)-(y**3+19*x**5)/(32*y**3-math.sin(x))

def zad1_2(x):
    if x<109:
        return ((39*x**4-math.exp(x))**3)-75*x**6
    elif 109<=x<194:
        return abs(x**5-x**2)+75*x
    else:
        return x**6 + math.log(x)+61

def zad1_3(n,m):
    sum1=sum2=0
    for i in range (1,n+1):
        for j in range (1,m+1):
            sum1+=89*j**4+2*j**3+68
    for i in range (1,n+1):
        sum2+=i-math.exp(i)
    return 23*sum1-sum2

def zad1_4(n):
    if n==0:
        return 5
    elif n==1:
        return 9
    else:
        return math.tan(zad1_4(n-2))+(zad1_4(n-2))/37+31

print("Задание 1_1",zad1_1(-39,17), zad1_1(-88,81), sep='\n',end="\n=======================\n")

print("Задание 1_2",zad1_2(120), zad1_2(47), sep='\n',end="\n=======================\n")

print("Задание 1_3",zad1_3(51,76), zad1_3(91,61), sep='\n',end="\n=======================\n")

print("Задание 1_4",zad1_4(9), zad1_4(7), sep='\n')
