import sys

def result(n, wines):
  if n < 3:
    return sum(wines)
  
  table = [0, wines[1], wines[1]+wines[2]]
  for i in range(3, n+1):
    table.append(max(table[i-1],
                    max(table[i-2]+wines[i],
                    table[i-3]+wines[i-1]+wines[i])))

  return table[n]


n = int(sys.stdin.readline())

wines = [0] + [int(sys.stdin.readline()) for _ in range(n)]
print(result(n, wines))
