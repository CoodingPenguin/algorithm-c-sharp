def fibb(n):
      if n <= 1:
    return n
  fibb = [0, 1]
  for i in range(2, n+1):
    fibb.append(fibb[i-2]+fibb[i-1])
  return fibb[n]

n = int(input())
print(fibb(n))