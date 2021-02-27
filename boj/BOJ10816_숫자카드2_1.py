import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def count(lst, value):
    right_idx = bisect_right(lst, value)
    left_idx = bisect_left(lst, value)
    return right_idx - left_idx


N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))
result = [str(count(cards, num)) for num in checks]
print(" ".join(result))

