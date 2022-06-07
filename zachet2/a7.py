def main(x):
    a = x & 0b1111_1111_1111
    b = (x >> 12) & 0b1111_1111_111
    c = (x >> 23) & 0b1111_111
    d = (x >> 30) & 0b1
    e = (x >> 31) & 0b0
    result = a | (b << 12) | (e << 23) | (c << 24) | (d << 31)
    return result
print(hex(main(0x452b3ae9)))