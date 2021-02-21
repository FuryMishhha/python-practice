def naive_mul(x, y):
    r = 0
    for i in range(0, y):
        r+=x
    return r

def test_naive_mul():
    for x in range(101):
        for y in range(101):
            assert x * y == naive_mul(x, y)
    print("Everything all right!(naive_nul)")

