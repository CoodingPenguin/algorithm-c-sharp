import sys
from itertools import combinations


n, m = map(int, sys.stdin.readline().split())
nums = range(1, n+1)
combine = list(combinations(nums, m))

for i in combine:
    i = map(str, i)
    print(' '.join(i))
