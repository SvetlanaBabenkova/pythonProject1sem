import math
def main(x):
    if x < -35:
        ans = (12 * x - 1) ** 7 + x ** 5
    elif x >= 135:
        ans = math.cos(x) ** 5
    elif (x <= -35) & (x < -15):
        ans = 71 * x ** 4
    elif (x <= -15) & (x < 37):
        ans = (x ** 2 + 44) ** 6 + x + ((math.cos(x + 1 + 10 * x ** 3)) ** 3)
    else:
        ans = 6 * x ** 7
    return ans
print(main(122))