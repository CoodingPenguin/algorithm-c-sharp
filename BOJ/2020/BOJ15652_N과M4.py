import sys
from itertools import combinations_with_replacement


n, m = map(int, sys.stdin.readline().split())
nums = range(1, n+1)
results = list(combinations_with_replacement(nums, m))

for i in results:
    i = map(str, i)
    print(' '.join(i))
