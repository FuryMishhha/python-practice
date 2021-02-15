import math

def zad1_2(x):
    if x<109:
        return ((39*x**4-math.exp(x))**3)-75*x**6
    elif 109<=x<194:
        return abs(x**5-x**2)+75*x
    else:
        return x**6 + math.log(x)+61

print(f'{zad1_2(120):.2e}', f'{zad1_2(47):.2e}', sep='\n')
