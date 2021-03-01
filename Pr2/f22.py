def f22(x):
    a = x & 0x00000003
    b = x & 0x0003fffc
    c = x & 0x00fc0000
    d = x & 0x7f000000
    e = x & 0x80000000
    a = a << 16
    b = b >> 2
    c = c << 1
    d = d << 1
    e = e >> 13
    x = a + b + c + d + e
    return x

print(f'{f22(0xadcb40f2):#x}')
print(f'{f22(0xa9e27ff0):#x}')

