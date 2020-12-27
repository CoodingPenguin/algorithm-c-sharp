from collections import deque
import sys

input = sys.stdin.readline


if __name__ == "__main__":
  n, m = map(int, input().rstrip().split())
  dq = deque(range(1, n+1))
  order = list(map(int, input().rstrip().split()))
  
  count = 0
  for target in order:
    l = len(dq)
    idx = dq.index(target)

    if idx < l-idx+1:
      while dq[0] != target:
        dq.rotate(-1)
        count += 1
    else:
      while dq[0] != target:
        dq.rotate(1)
        count += 1
    
    dq.popleft()
  
  print(count)
