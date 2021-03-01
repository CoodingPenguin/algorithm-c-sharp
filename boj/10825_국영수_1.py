import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  name, korean, english, math = input().rstrip().split()
  arr.append((int(korean), int(english), int(math), name))
arr.sort(key=lambda x:x[3])
arr.sort(reverse=True, key=lambda x:x[2])
arr.sort(key=lambda x:x[1])
arr.sort(reverse=True, key=lambda x:x[0])
for i in range(n):
  print(arr[i][3])