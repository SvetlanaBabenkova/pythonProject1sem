def main(x):
    a = x & 0b1111_1111_1111_1
    b = (x >> 13) & 0b1111_1111_1111_111
    c = (x >> 28) & 0b1
    d = (x >> 29) & 0b111
    result = c | (a << 16) | (b << 1) | (d << 29)
    return result

print(hex(main(0x988dba6a)))