def move(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        move(n-1, start, end, mid)
        print(start, end)
        move(n-1, mid, start, end)


N = int(input())
print((2**N)-1)
move(N, 1, 2, 3)
