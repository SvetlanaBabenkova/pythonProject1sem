from struct import *

FMT = dict(  # standard size
    char='c',  # 1
    int8='b',  # 1
    uint8='B',  # 1
    int16='h',  # 2
    uint16='H',  # 2
    int32='i',  # 4
    uint32='I',  # 3
    int64='q',  # 8
    uint64='Q',  # 8
    float='f',  # 4
    double='d'  # 8
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1 = unpack('>H', buf[offs: offs + 2])[0]
    a2 = unpack('>I',buf[offs + 14:offs + 18])[0]
    a3 = unpack('>f', buf[offs + 4: offs + 8])[0]
    a4 = unpack('>f', buf[offs + 4: offs + 8])[0]
    offs += 8
    f4 = unpack('>II', buf[offs: offs + 8])
    for i in range(f4[0]):
        a4 = ''.join(map(str, unpack(f'>{f4[0]}c', buf[f4[1]: f4[1] + 2])))
    a4 = a4.replace('\'b', '', 1)
    a4 = a4.replace('\'', '')
    a4 = a4.replace('b', '', 1)
    a5, offs = parse_d(buf, offs)
    a6 = unpack('>Q', buf[offs: offs + 8])[0]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6), offs


def parse_b(buf, offs):
    b1 = unpack('>i', buf[offs: offs + 4])[0]
    offs += 4
    b2 = unpack('>B', buf[offs: offs + 1])[0]
    offs += 1
    b3 = " ".join(map(str, unpack('>5c', buf[offs: offs + 5])))
    offs += 5
    b3 = b3.replace('\' ', '')
    b3 = b3.replace('b\'', '')
    b3 = b3.replace('\'', '')
    f1 = unpack('>II', buf[offs: offs + 8])
    b4 = list()
    for i in range(f1[0]):
        f2 = unpack('>H', buf[f1[1] + 2 * i: f1[1] + 2 + 2 * i])
        b4.append(parse_c(buf, f2[0]))

    return dict(B1=b1, B2=b2, B3=b3, B4=b4), offs


def parse_c(buf, offs):
    c1 = unpack('>b', buf[offs: offs + 1])[0]
    c2 = unpack('>d', buf[offs + 1: offs + 9])[0]
    c3 = unpack('>b', buf[offs + 9: offs + 10])[0]
    return dict(C1=c1, C2=c2, C3=c3)


def parse_d(buf, offs):
    offs += 8
    d1 = unpack('>Q', buf[offs: offs + 8])[0]
    f2 = unpack('>IH', buf[offs + 8: offs + 14])
    d2 = list(unpack(f'>{f2[0]}B', buf[f2[1]:f2[1] + f2[0] + 7]))
    d3 = unpack('>I', buf[offs + 14:offs + 18])[0]
    d4 = list(unpack('>7h', buf[offs + 18:offs + 32]))
    d5 = unpack('>I', buf[offs + 32: offs + 36])[0]
    d6 = unpack('>f', buf[offs + 36: offs + 40])[0]
    d7 = unpack('>h', buf[offs + 40: offs + 42])[0]
    d8 = unpack('>Q', buf[offs + 42: offs + 50])[0]
    offs += 50
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6, D7=d7, D8=d8), offs


def main(buf):
    return parse_a(buf, 5)[0]


#######

print(main())