import math


def main(x, z, y):
    ans = 0
    for i in range(len(x)):
        ans += 32 * (z[len(x) + 1 - i] ** 3 - 53 * x[len(x) + 1 - [i // 4]] ** 2 - y[len(x) + 1 - i] ** 2)
    ans *= 22
    return ans


print(main([0.77, 0.09, -0.18], [0.92, -0.11, 0.66], [0.99, -0.65, 0.44]))
