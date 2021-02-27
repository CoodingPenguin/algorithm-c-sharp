import sys

input = lambda: sys.stdin.readline().rstrip()


a_arr, b_arr = [], []

n, m = map(int, input().split())
for _ in range(n):
  a_arr.append(list(map(int, input().split())))

_, k = map(int, input().split())
for _ in range(m):
  b_arr.append(list(map(int, input().split())))

mult = [[0]*k for _ in range(n)]
for i in range(n):
  for j in range(k):
    a_items = a_arr[i]
    b_items = [row[j] for row in b_arr]
    print(sum([a*b for a, b in zip(a_items, b_items)]), end=" ")
  print()