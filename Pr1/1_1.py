import math

def zad1_1(x,y):
    return (79*x**3-24*y**6)/(y**5+abs(y))+(2*x**8-y**7)/(2*x**7+x**8)-(y**3+19*x**5)/(32*y**3-math.sin(x))

print("Задание 1_1",zad1_1(-39,17), zad1_1(-88,81), sep='\n')
