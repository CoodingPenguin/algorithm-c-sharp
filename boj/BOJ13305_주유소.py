import sys

input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

pred = cost[0]
result = 0
for i in range(len(dist)):
    if cost[i] < pred:
        pred = cost[i]
    result += dist[i] * pred

print(result)
