import math


def main(m, a, x):
    ans = 0
    for i in range (1, a+1):
        for c in range (1, m+1):
            ans += (63 * x ** 2 + c + 73 * (i / 39 + 85 + 93 * i ** 2) ** 7)
    return ans

res = main(7, 5, 0.04)
print(res)