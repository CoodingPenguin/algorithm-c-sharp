# 풀이 1
import math


def add_all(limit):
    return sum(list(range(1, limit+1)))


def my_number(n):
    m = int(math.sqrt(2*n))
    n -= add_all(m)
    while True:
        if n <= 0:
            break
        m += 1
        n -= m
    return m, (n+m)


def result(s, e):
    ss, ee = my_number(s), my_number(e)
    rt = 0
    if ss[0] == ee[0]:
        rt += ss[0] * (ee[1] - ss[1]+1)
    else:
        for i in range(ss[0]+1, ee[0]):
            rt += i*i
        rt += (ss[0] - ss[1] + 1) * ss[0] + ee[1] * ee[0]
    return rt


_ = list(map(int, input().split()))
s, e = _[0], _[1]

if s == e:
    print(my_number(s)[0])
else:
    print(result(s, e))
