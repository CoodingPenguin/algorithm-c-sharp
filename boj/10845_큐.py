import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    command = input().rstrip()
    num = None
    if "push" in command:
        command, num = command.split()

    if command == "push":
        q.append(num)
    elif command == "pop":
        try:
            temp = q.popleft()
            print(temp)
        except:
            print(-1)
    elif command == "size":
        print(len(q))
    elif command == "empty":
        if not len(q):
            print(1)
        else:
            print(0)
    elif command == "front":
        try:
            temp = q.popleft()
            print(temp)
            q.appendleft(temp)
        except:
            print(-1)
    else:
        try:
            temp = q.pop()
            print(temp)
            q.append(temp)
        except:
            print(-1)
