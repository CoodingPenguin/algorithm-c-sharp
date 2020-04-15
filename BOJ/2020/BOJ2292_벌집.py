n = int(input())
rt = 1

while n > 1:
    n -= 6*rt
    rt += 1

print(rt)
