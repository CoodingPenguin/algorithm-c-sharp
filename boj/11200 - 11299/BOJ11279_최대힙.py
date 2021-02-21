import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(q, -x)
    else:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)

