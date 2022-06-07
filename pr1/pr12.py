import struct


def parse_array(data, size, typ, offset):  # Unpacking an array
    n = struct.calcsize(typ)
    return list(struct.unpack(f'<{size}{typ}', data[offset: offset + size * n]))


def parse_array_struct_c(data, size, offset):  # Unpacking a struct-array C
    arr = list()
    for count in range(size):
        arr.append(parse_c(data, offset + count * 12))  # 12 = size of struct C
    return arr


def parse_d(data, offset):
    d1 = parse_array(data, 2, 'b', offset)  # Unpacking an array
    d2 = struct.unpack('<I', data[offset + 2: offset + 2 + 4])[0]  # little-endian: < , big-endian: >
    d3 = struct.unpack('<b', data[offset + 6: offset + 6 + 1])[0]
    d4 = struct.unpack('<q', data[offset + 7: offset + 7 + 8])[0]
    d5 = struct.unpack('<H', data[offset + 15: offset + 15 + 2])[0]
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4, 'D5': d5}


def parse_c(data, offset):
    c1 = struct.unpack('<f', data[offset: offset + 4])[0]
    c2 = parse_array(data, 2, 'f', offset + 4)  # f = 4
    return {'C1': c1, 'C2': c2}  # c = 12


def parse_b(data, offset):
    b1 = struct.unpack('<B', data[offset: offset + 1])[0]  # B = 1, H = 2, I = 4
    b2_size, b2_offset = struct.unpack('<HI',
                                       data[offset + 1: offset + 1 + 2 + 4])
    b2 = parse_array(data, b2_size, 's', b2_offset)
    b2 = b2[0].decode()
    # print("b2:", b2, type(b2), type(b2[0]))
    b3 = struct.unpack('<q', data[offset + 7: offset + 7 + 8])[0]
    b4 = struct.unpack('<B', data[offset + 15: offset + 15 + 1])[0]
    b5 = struct.unpack('<q', data[offset + 16: offset + 16 + 8])[0]
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5}


def parse_a(data, offset):
    a1 = struct.unpack('<H', data[offset: offset + 2])[0]
    a2 = struct.unpack('<I', data[offset + 2: offset + 2 + 4])[0]
    a3_offset = struct.unpack('<H', data[offset + 6: offset + 6 + 2])[0]
    a3 = parse_b(data, a3_offset)
    a4 = struct.unpack('<Q', data[offset + 8: offset + 8 + 8])[0]
    a5 = parse_array_struct_c(data, 8, offset + 16)  # 96 = size array of struct C*8
    a6_offset = struct.unpack('<I', data[offset + 112: offset + 112 + 4])[0]
    a6 = parse_d(data, a6_offset)
    a7 = struct.unpack('<Q', data[offset + 116: offset + 116 + 8])[0]
    # Ctrl + D - copy current line
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5,
            'A6': a6, 'A7': a7}


def main(data):
    return parse_a(data, 5)  # offset = 5


inp_1 = (b'\x90GVDO\x9e\xd9\xd1\xe0\xd2\xb9\x86\x00\xea52\xf1\xdc\x9dO\xe2\\_B'
         b'\xbf\xcf\xed\x12\xbep\xf4p\xbfbeT\xbe+'
         b'\xfec\xbf\x94\x03\xc7\xbe\xa1\xe5\x94'
         b'=\xbb(v?I\xcf\'\xbf.\x0ev?"h&\xbf\x02'
         b'\x9a\xf2\xbe"\x0e\xec=\x16x=?\xbbg\x1d'
         b'\xbeCg\xb2\xbe\x06)\x83>3\xe7A>\x1d\xa8\n'
         b'\xbf\x01\xbe\xc8\xbe\xa3\x976'
         b'\xbf/\xab_?@\xa8e\xbf\x17\x0e\xd4<\x9e'
         b'\x00\x00\x00,e\x8b\\\xeb+\x16\x1fojh'
         b'lgt\x05\x00\x81\x00\x00\x005*\x1c\xbd\x8e'
         b'\xb1\x91.GV\xb2=\xa0\x06\xc8'
         b'\xdc\xa9\xb8\xce\\\xc4Qn\xb4\xc1\xf7\xdd\xda\nbL\xd0:\x93')

main(inp_1)
