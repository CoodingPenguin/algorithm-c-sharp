def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


nums = list(map(int, input().split()))
x, y = max(nums), min(nums)

GCD = gcd(x, y)
LCM = x*y//GCD
print(GCD)
print(LCM)
