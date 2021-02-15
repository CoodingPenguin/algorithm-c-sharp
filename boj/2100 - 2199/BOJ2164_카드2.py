from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
  n = int(input().rstrip())
  dq = deque(list(range(1, n+1)))
  
  while len(dq) > 1:
    dq.popleft()
    dq.rotate(-1)
  
  print(dq[-1])
