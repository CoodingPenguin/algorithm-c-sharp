import sys
from itertools import product


n, m = map(int, sys.stdin.readline().split())
nums = range(1, n+1)
results = list(product(nums, repeat=m))

for i in results:
    i = map(str, i)
    print(' '.join(i))
