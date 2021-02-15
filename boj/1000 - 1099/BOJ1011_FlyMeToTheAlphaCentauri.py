import math


def result(x, y):
    diff = y-x
    root = int(math.sqrt(diff))

    if diff == root**2:
        return 2*root-1
    elif diff > (root**2 + (root+1)**2)//2:
        return 2*root+1
    else:
        return 2*(root)


for _ in range(int(input())):
    x, y = map(int, input().split())
    print(result(x, y))
