import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
cards = Counter(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))
result = [str(cards[num]) for num in checks]
print(" ".join(result))

