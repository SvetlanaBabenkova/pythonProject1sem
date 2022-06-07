import math
def main(y, x):
    ans = (67 * (38 * y ** 2 + x ** 3 + 1) ** 4) - (math.tan(x) ** 7) - \
          ((y ** 9 + 59 * x ** 5) / (((62 * y ** 2 + y ** 3) ** 3) - \
                                     (22 * x ** 3 -38 * x - (((y ** 2) / 89) ** 7) / 3)))
    return ans
print(main(-0.45, -0.76))