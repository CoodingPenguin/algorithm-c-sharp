apt = [[0]*14 for _ in range(15)]
for i in range(14):
    apt[0][i] = i+1
for i in range(1, 15):
    for j in range(14):
        if j == 0:
            apt[i][j] = 1
            continue
        apt[i][j] = apt[i-1][j]+apt[i][j-1]

for _ in range(int(input())):
    k, n = int(input()), int(input())
    print(apt[k][n-1])
