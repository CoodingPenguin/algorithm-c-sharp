import sys


N = int(sys.stdin.readline())
table = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
  row = list(map(int, sys.stdin.readline().split()))
  for j in range(1, i+1):
    table[i][j] = max(table[i-1][j-1], table[i-1][j])+row[j-1]

print(max(table[N]))
