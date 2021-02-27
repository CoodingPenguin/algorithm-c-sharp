import sys
from itertools import permutations


n, m = map(int, sys.stdin.readline().split())
nums = range(1, n+1)
permute = list(permutations(nums, m))

for i in permute:
    i = map(str, i)
    print(' '.join(i))
