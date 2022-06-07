def main(x):
    if x[1] == 1987:
        return x2_2(x)
    elif x[1] == 1996:
        return x3_3(x)

def x2_2(x):
    if x[2] == 'JFLEX':
        return x0_3(x)
    elif x[2] == 'LIFE':
        return x0_3_1(x)

def x3_3(x):
    if x[3] == 'ASP':
        return x2_2_1(x)
    elif x[3] == 'AWK':
        return 8
    elif x[3] == 'ANTLR':
        return 9

def x0_3(x):
    if x[0] == 'ANTLR':
        return 0
    elif x[0] == 'MAX':
        return 1
    elif x[0] == 'DIFF':
        return 2

def x0_3_1(x):
    if x[0] == 'ANTLR':
        return 3
    elif x[0] == 'MAX':
        return 4
    elif x[0] == 'DIFF':
        return 5

def x2_2_1(x):
    if x[2] == 'JFLEX':
        return 6
    elif x[2] == 'LIFE':
        return 7

print(main(['DIFF', 1996, 'LFE', 'AWK']))