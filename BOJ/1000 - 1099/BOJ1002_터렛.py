import math


def cal_dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


def cal_pos(x1, y1, r1, x2, y2, r2):
    cenDist = cal_dist(x1, y1, x2, y2)
    if cenDist > r1+r2 or cenDist < abs(r1-r2):
        return 0
    elif cenDist < r1+r2 and cenDist > abs(r1-r2):
        return 2
    elif cenDist == 0 and r1 == r2:
        return -1
    else:
        return 1


for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(cal_pos(x1, y1, r1, x2, y2, r2))
