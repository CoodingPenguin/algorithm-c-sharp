import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  arr.append(input().split())
arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for item in arr:
  print(item[0])