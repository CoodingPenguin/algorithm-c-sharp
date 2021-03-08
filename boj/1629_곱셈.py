import sys

input = sys.stdin.readline

# 퀵소트처럼 반으로 나눠서 logN만큼 걸림
def power(exp, n):
    if n == 1:
        return exp % rest
    power_of_half = power(exp, n // 2)
    if n % 2 == 0:
        return (power_of_half ** 2) % rest
    else:
        return (power_of_half ** 2) * exp % rest


exp, n, rest = map(int, input().split())
print(power(exp, n))
