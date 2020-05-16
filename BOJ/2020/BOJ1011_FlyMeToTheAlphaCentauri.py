def result(x, y):
    diff = y-x
    if diff < 3:
        return diff
    rt, diff = 2, diff-1
    while diff != 1:
        diff //= 2
        rt += 1
    return rt


for _ in range(int(input())):
    x, y = map(int, input().split())
    print(result(x, y))
