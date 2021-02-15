n = int(input())
rt = 0

while n > 0:
    if n % 5 == 0:
        rt += n//5
        break
    elif n < 3:
        rt = -1
        break
    n -= 3
    rt += 1
print(rt)
