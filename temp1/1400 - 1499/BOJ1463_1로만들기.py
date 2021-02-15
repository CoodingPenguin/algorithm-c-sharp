n = int(input())
table = [0] * (n+1)

for i in range(2, n+1):
  table[i] = table[i-1]+1

  if i%2 == 0:
    table[i] = min(table[i], table[i//2]+1)
  
  if i%3 == 0:
    table[i] = min(table[i], table[i//3]+1)

print(table[-1])