def result(i, j):
    while i != 0:
        if i%3 == 1 and j%3 == 1:
            print(' ', end='')
            return
        i, j = i//3, j//3
    print("*", end="")

N = int(input())
for i in range(N):
    for j in range(N):
        result(i, j)
    print()