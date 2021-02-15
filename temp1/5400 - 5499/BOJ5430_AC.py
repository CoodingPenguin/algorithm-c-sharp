from collections import deque
import sys

input = sys.stdin.readline

def parse_commands(commands):
  stack = []
  for c in commands:
    if c == "R":
      if not stack or stack[-1] == "D":
        stack.append("R")
      else:
        stack.pop()
    else:
      stack.append("D")
  return stack

def parse_list(string):
  if string == "[]":
    return list()
  lst = string.replace("[", "").replace("]", "").split(",")
  return lst


def handle_command(commands, dq):
  is_reversed = False
  for c in commands:
    if c == "R":
      is_reversed = not is_reversed
    else:
      try:
        if is_reversed:
          dq.pop()
        else:
          dq.popleft()
      except:
        return "error"
  
  if is_reversed:
    dq.reverse()
  return "[" + ",".join(dq) + "]"


if __name__ == "__main__":
  tc = int(input().rstrip())
  for _ in range(tc):
    commands = parse_commands(input().rstrip())
    _ = input()
    dq = deque(parse_list(input().rstrip()))
    
    print(handle_command(commands, dq))