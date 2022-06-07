def main(x):
    a = x & 0b1111
    b = (x >> 4) & 0b1111_111
    c = (x >> 11) & 0b1111_1
    d = (x >> 16) & 0b1111_1111_1111_111
    e = (x >> 31) & 0b1
    result = c | (a << 21) | (b << 25) | (d << 6) | (e << 5)
    return result


print(main(0x988dba6a))