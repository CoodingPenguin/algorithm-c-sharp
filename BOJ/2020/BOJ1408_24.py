def one2two(digit):
    if len(digit) == 1:
        return "0" + digit
    else:
        return digit


def result(pt, st):
    rt = ""
    second, minute, hour = 0, 0, 0
    sc, mc = 0, 0

    if st[2] - pt[2] >= 0:
        second = st[2] - pt[2]
    else:
        second = st[2] - pt[2] + 60
        sc = 1

    if st[1] - pt[1] - sc >= 0:
        minute = st[1] - pt[1] - sc
    else:
        minute = st[1] - pt[1] - sc + 60
        mc = 1

    if st[0] - pt[0] - mc >= 0:
        hour = st[0] - pt[0] - mc
    else:
        hour = st[0] - pt[0] - mc + 24

    return one2two(str(hour)) + ":" + one2two(str(minute)) + ":" + one2two(str(second))


presentTime = list(map(int, input().split(":")))
startTime = list(map(int, input().split(":")))

print(result(presentTime, startTime))
