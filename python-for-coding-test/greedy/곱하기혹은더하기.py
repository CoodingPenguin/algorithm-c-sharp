import sys

input = sys.stdin.readline
s = input().rstrip()
result = 0
for i, num in enumerate(s):
    num = int(num)
    if i == 0:
        result += num
    else:
        if result < 2 or num < 2:
            result += num
        else:
            result *= num
print(result)
