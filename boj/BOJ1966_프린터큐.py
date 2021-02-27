from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
  tc = int(input().rstrip())
  for _ in range(tc):
    n, m = map(int, input().rstrip().split())
    queue = deque(map(int, input().rstrip().split()))

    count = 0
    while queue:
      # 최대값 구하기
      max_item = max(queue)
      # 최대값이 가장 앞에 올 때까지 회전
      while queue[0] != max_item:
        queue.rotate(-1)
        m -= 1
        if m < 0:
          m += len(queue)
      # 최대값을 만나면 pop
      queue.popleft()
      count += 1
      m -= 1
      if m < 0:
        break
    
    print(count)