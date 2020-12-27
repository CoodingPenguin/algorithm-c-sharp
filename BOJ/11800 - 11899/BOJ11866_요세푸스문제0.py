from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
  n, k = map(int, input().rstrip().split())
  dq = deque(range(1, n+1))
  result = list()

  while dq:
    dq.rotate(-k+1)
    result.append(dq.popleft())
  
  print("<" + ", ".join(map(str, result)) + ">")
