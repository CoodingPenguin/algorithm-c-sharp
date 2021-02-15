n = int(input())
result = [1]*(n+1)
for i in range(2, n+1):
  result[i] = (result[i-1] + result[i-2])%15746

print(result[n])