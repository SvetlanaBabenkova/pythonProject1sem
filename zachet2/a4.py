import math
def main(n):
    if n == 0:
        return 0.97
    elif n == 1:
        return 0.88
    elif n >= 2:
        return main(n-2) ** 2 + main(n-2) + ((main(n-1) ** 3) / 69)

print(main(5))