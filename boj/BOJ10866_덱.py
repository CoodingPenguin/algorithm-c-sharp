from collections import deque
import sys

input = sys.stdin.readline

def handle_command(dq, command, item):
  if command == "push_front":
    dq.appendleft(item)
  elif command == "push_back":
    dq.append(item)
  elif command == "pop_front":
    if dq:
      print(dq.popleft())
    else:
      print(-1)
  elif command == "pop_back":
    if dq:
      print(dq.pop())
    else:
      print(-1)
  elif command == "size":
    print(len(dq))
  elif command == "empty":
    if not dq:
      print(1)
    else:
      print(0)
  elif command == "front":
    if dq:
      print(dq[0])
    else:
      print(-1)
  else:
    if dq:
      print(dq[-1])
    else:
      print(-1)


if __name__ == "__main__":
  n = int(input().rstrip())
  dq = deque()
  for _ in range(n):
    # 명령어 입력
    command_item = input().rstrip().split()
    command = command_item[0]
    item = None
    if len(command_item) > 1:
      item = int(command_item[1])
    handle_command(dq, command, item)