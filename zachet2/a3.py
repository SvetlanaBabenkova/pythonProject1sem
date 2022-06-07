import math
def main(b, n, a):
    ans = 0
    for i in range(1, a+1):
        for j in range(1, n+1):
            for k in range(1, b+1):
                ans += (math.log10(j) ** 2 + (83 * k ** 3 - 51 - (i / 86)) ** 5)
    return ans
print(main(3, 4, 2))