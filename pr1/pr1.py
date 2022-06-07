import math


def main(n, b, a, z):
    ans = 0
    for c in range(1, a + 1):
        for k in range(1, b + 1):
            for i in range(1, n + 1):
                A = math.pow((math.fabs(k * k - c)), 3)
                B = math.pow(i, 2)
                C = math.pow((33 * z * z - math.pow(i, 3)), 4)
                ans += A - B - C
    return ans


print(main(7, 5, 7, 0.71))
print(main(2, 7, 4, 0.72))
