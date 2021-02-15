import sys

input = sys.stdin.readline

table = [[0] * 31 for j in range(31)]
for i in range(1, 31):
    for j in range(1, 31):
        if 1 in (i, j):
            table[i][j] = i * j
        elif i == j:
            table[i][j] = 1
        elif i < j:
            table[i][j] = sum(table[i - 1][i - 1 : j])
        else:
            table[i][j] = table[j][i]


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(table[n][m])

