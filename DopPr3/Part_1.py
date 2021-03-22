# №1 whitespace before '('
for i in range (337):
    print(i)

# №2 missing whitespace around operator
b= 5

# №3 missing whitespace after ','.
c = [1,2,3,4,5]

# №4 unexpected spaces around keyword / parameter equals
def func1(p = 4):
    print("auf")

# №5 expected 2 blank lines, found 1
def func2():
    return

# №6 multiple statements on one line (colon)
if c > 100: print("pr6")

# №7 multiple statements on one line (semicolon)
d = 1; e = 2

# №8 comparison to None should be 'if cond is None:'
if d == None:
    print("pr8")

# №9 comparison to True should be 'if cond is True:' or 'if cond:'
if e == True:
    print("pr9")

'''
=============Логи сайта pep8online.com=============
Code	Line	Column	Text
E211	2	    15	    whitespace before '('
E225	6	    2	    missing whitespace around operator
E231	9	    7	    missing whitespace after ','
E231	9	    9	    missing whitespace after ','
E231	9	    11	    missing whitespace after ','
E231	9	    13	    missing whitespace after ','
E302	12	    1	    expected 2 blank lines, found 1
E251	12	    12	    unexpected spaces around keyword / parameter equals
E251	12	    14	    unexpected spaces around keyword / parameter equals
E302	16	    1	    expected 2 blank lines, found 1
E701	20	    11	    multiple statements on one line (colon)
E702	23	    6	    multiple statements on one line (semicolon)
E711	26	    6	    comparison to None should be 'if cond is None:'
E712	30	    6	    comparison to True should be 'if cond is True:' or 'if cond:'
'''