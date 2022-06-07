import math
def main(y, x):
    ans = 0
    for i in range (len(x)):
        ans += (math.tan((y[len(x) - 1 - i]) ** 3 - 99 - x[i // 2])) ** 4
    return ans

print(main([-0.7, 0.91, 0.22, 0.91, -0.97, 0.44, 0.36, 0.93],
     [-0.96, -0.06, -0.23, -0.82, -0.18, 0.0, 0.73, 0.14]))