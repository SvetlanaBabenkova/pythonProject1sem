def main(x):
    if x[1] == 'KRL':
        return x3_1(x)
    elif x[1] == 'GAP':
        return 13
    elif x[1] == 'RED':
        return 14


def x3_1(x):
    if x[3] == 1999:
        return x4_3(x)
    elif x[3] == 1979:
        return x4_3_1(x)
    elif x[3] == 1963:
        return 12


def x4_3(x):
    if x[4] == 'JSX':
        return 0
    elif x[4] == 'MUF':
        return x2_3_1(x)
    elif x[4] == 'SMT':
        return x2_3_2(x)


def x4_3_1(x):
    if x[4] == 'JSX':
        return 7
    elif x[4] == 'MUF':
        return x2_3_3(x)
    elif x[4] == 'SMT':
        return 11


def x2_3_1(x):
    if x[2] == 'GOLO':
        return 1
    elif x[2] == 'OPA':
        return 2
    elif x[2] == 'MESON':
        return 3


def x2_3_2(x):
    if x[2] == 'GOLO':
        return 4
    elif x[2] == 'OPA':
        return 5
    elif x[2] == 'MESON':
        return 6


def x2_3_3(x):
    if x[2] == 'GOLO':
        return 8
    elif x[2] == 'OPA':
        return 9
    elif x[2] == 'MESON':
        return 10


print(main([2013, 'KRL', 'MESON', 1979, 'JSX']))