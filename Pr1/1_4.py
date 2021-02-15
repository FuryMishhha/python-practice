import math

def zad1_4(n):
    if n==0:
        return 5
    elif n==1:
        return 9
    else:
        return math.tan(zad1_4(n-2))+(zad1_4(n-2))/37+31

print("Задание 1_4",zad1_4(9), zad1_4(7), sep='\n')
