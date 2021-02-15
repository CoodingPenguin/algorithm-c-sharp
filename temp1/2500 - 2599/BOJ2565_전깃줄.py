n = int(input())
lines = [(0, 0)]
for _ in range(n):
  a, b = map(int, input().split())
  lines.append((a, b))
lines.sort()

table = [0] + [1]*n
for i in range(1, n+1):
  for j in range(i):
    if lines[j][1] < lines[i][1] and table[i] < table[j]+1:
      table[i] = table[j] + 1

print(n - max(table))
