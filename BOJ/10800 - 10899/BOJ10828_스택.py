import sys

input = sys.stdin.readline
n = int(input())
stack = list()

for _ in range(n):
  command = input().strip().split()
  method, item = command[0], None
  if len(command) > 1:
    item = command[1]
  
  if method == "push":
    stack.append(item)
  elif method == "top":
    if not stack:
      print(-1)
    else:
      print(stack[-1])
  elif method == "pop":
    if not stack:
      print(-1)
    else:
      print(stack.pop())
  elif method == "size":
    print(len(stack))
  else:
    if not stack:
      print(1)
    else:
      print(0)