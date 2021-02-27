import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

result = 0
start, end = 0, max(trees)
while start <= end:
    mid = (start + end) // 2
    rest_of_tree = sum([tree - mid for tree in trees if tree > mid])
    if rest_of_tree < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
