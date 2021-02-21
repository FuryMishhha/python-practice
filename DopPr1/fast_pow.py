def fast_pow(x, y):
    r = 1
    while y > 0:
        if y == 1:
            return r * x
        if y % 2 != 0:
            r *= x
        x *= x
        y //= 2
    return r

def test_fast_pow():
    for x in range(101):
        for y in range(101):
            assert x ** y == fast_pow(x, y)
    print("Everything all right!(fast_pow)")