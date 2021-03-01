from Table import Table
n=int(input())
a=[Table]*n
print(a)

for i in range(n):
    nu, na, em = input().split()

    def display_table(self):
        print('{} {} {}'.format(self.number, self.name, self.email))


2
0.005 lfnufi xwfuadww
0.5 ddnidi xwfuad
0.34 lfnufi xwfua
0.254 lfnufi xwfuadww

import operator
class Table():
    def __init__(self, number, name, email):
        self.number = name
        self.name = name
        self.email = email

    def display_table(self):
        print('{} {} {}'.format(self.number, self.name, self.email))

n = int(input())

objects = []

"""
for i in range(n):
    nu, na, em = input().split()
    st = Table(nu, na, em)
    objects.append(st)
"""

el1 = Table(0.005, "lfnufi", "xwfuadww")
el2 = Table(0.5, "ddnidi", "xwfuad")
el3 = Table(0.34, "lfnufi", "xwfua")
el4 = Table(0.254, "lfnufi", "xwfuadww")

objects = [el1, el2, el3, el4]

for st1 in objects:
    x = 0
    for st2 in objects:
        if (st1.number == st2.number) & (st1.name == st2.name) & (st1.email == st2.email) & (x == 0):
            x += 1
        elif (st1.number == st2.number) & (st1.name == st2.name) & (st1.email == st2.email) & (x != 0):
            objects.remove(st2)
    print("NEXT")


for st in objects:
    print(st.display_table())