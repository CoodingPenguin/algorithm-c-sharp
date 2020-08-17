powerOfTwo = [2**x for x in range(0, 20)]


def move(n, start, end):
    if n == 1:
        print(start, end)
        return
    mid = 6-start-end
    move(n-1, start, mid)
    move(1, start, end)
    move(n-1, mid, end)


def result(N):
    print(sum(powerOfTwo[:N]))
    if N == 1:
        print(1, 3)
        return
    move(N-1, 1, 2)
    move(1, 1, 3)
    move(N-1, 2, 3)


N = int(input())
result(N)
