import sys

input = lambda: sys.stdin.readline().rstrip()

def is_all_same(n, arr):
  item = arr[0][0]
  for i in range(n):
    for j in range(n):
      if item != arr[i][j]:
        return False
  return True


def divide(n, arr):
  global count
  if n == 1:
    count[arr[0][0]] += 1
    return
  if is_all_same(n, arr):
    count[arr[0][0]] += 1
    return
  
  divide(n//2, [row[0:n//2] for row in arr[0:n//2]])
  divide(n//2, [row[n//2:n] for row in arr[0:n//2]])
  divide(n//2, [row[0:n//2] for row in arr[n//2:n]])
  divide(n//2, [row[n//2:n] for row in arr[n//2:n]])


n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))
count = [0, 0]
divide(n, arr)
print("{}\n{}".format(count[0], count[1]))