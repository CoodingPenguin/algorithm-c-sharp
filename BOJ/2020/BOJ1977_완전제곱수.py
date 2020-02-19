import math


def perfect_num(start, end):
    perfectNums = []

    s, e = int(math.sqrt(start)), int(math.sqrt(end))+1
    for i in range(s, e):
        if i*i >= start and i*i <= end:
            perfectNums.append(i*i)

    if len(perfectNums) == 0:
        print(-1)
        return

    print(sum(perfectNums))
    print(perfectNums[0])


M, N = int(input()), int(input())
perfect_num(M, N)
