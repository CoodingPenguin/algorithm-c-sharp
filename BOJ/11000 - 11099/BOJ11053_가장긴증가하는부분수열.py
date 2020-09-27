import sys


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
table = [1] * (n+1)

for i in range(2, n+1):
  maxCount = 0
  for j in range(1, i):
    if nums[j-1] < nums[i-1] and table[j] > maxCount:
      maxCount = table[j]
  table[i] = maxCount+1

print(max(table))