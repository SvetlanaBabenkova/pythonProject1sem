import math


def main(y, x):
    ans = 0
    for i in range (len(x)):
        ans += 2 * (80 * x[i // 4] + 67 * x[len(x) - 1 - i] ** 3 +y[i // 4] ** 2) ** 5
    ans *= 55
    return ans

print(main([-0.98, -0.05, -0.03, 0.23, 0.34, 0.0],
     [0.03, -0.36, -0.0, -0.89, 0.52, 0.55]))