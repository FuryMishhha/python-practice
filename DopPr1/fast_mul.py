def fast_mul(x, y):
    r = 0
    if x == 0 | y == 0:
        return 0
    while y > 0:
        if y % 2 == 1:
            r += x
        x *= 2
        y//=2
    return r

def test_fast_mul():
    for x in range(101):
        for y in range(101):
            assert x * y == fast_mul(x, y)
    print("Everything all right!(fast_mul)")