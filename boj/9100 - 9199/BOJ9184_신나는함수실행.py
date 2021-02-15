import sys

input = sys.stdin.readline

table = [[[1] * 21 for _ in range(21)] for __ in range(21)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                table[i][j][k] = 1
            elif i < j and j < k:
                table[i][j][k] = (
                    table[i][j][k - 1] + table[i][j - 1][k - 1] - table[i][j - 1][k]
                )
            else:
                table[i][j][k] = (
                    table[i - 1][j][k]
                    + table[i - 1][j - 1][k]
                    + table[i - 1][j][k - 1]
                    - table[i - 1][j - 1][k - 1]
                )


def result(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return table[20][20][20]
    return table[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {result(a, b, c)}")

