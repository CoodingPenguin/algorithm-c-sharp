import sys
from collections import Counter

input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  counter = Counter()
  for _ in range(n):
    _, cloth = input().rstrip().split()
    counter[cloth] += 1

  result = 1
  for item in counter:
    # 입을 수 있는 가지수 + 1
    # ex. a를 입는 경우, b를 입는 경우, 안 입는 경우
    result *= (counter[item]+1)

  print(result-1)
