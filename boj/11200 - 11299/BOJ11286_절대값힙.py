import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(q, (abs(x), x))
    else:
        if q:
            abs_x, x = heapq.heappop(q)
            print(x)
        else:
            print(0)

