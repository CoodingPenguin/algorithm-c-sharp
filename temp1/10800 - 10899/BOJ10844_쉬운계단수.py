n = int(input())
table = [[0]*10 for _ in range(n+1)]
table[1] = [0] + [1]*9

for i in range(2, n+1):
  for j in range(10):
    if j == 0:
      table[i][j] = (table[i-1][j+1])
    elif j == 9:
      table[i][j] = table[i-1][j-1]
    else:
      table[i][j] = table[i-1][j-1] + table[i-1][j+1]

print(sum(table[n]) % 1000000000)
