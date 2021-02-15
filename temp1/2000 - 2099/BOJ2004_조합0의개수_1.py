import sys
from collections import Counter

input = sys.stdin.readline

def count_n(num, c):
  result = 0
  power_of_c = c
  while num >= power_of_c:
    result += num//power_of_c
    power_of_c *= c
  return result


def check_zero(n, m):
  if m == 0:
    return 0
  fives = count_n(n, 5) - count_n(m, 5) - count_n(n-m, 5)
  twos = count_n(n, 2) - count_n(m, 2) - count_n(n-m, 2)
  return min(fives, twos)
  

if __name__ == "__main__":
  n, m = map(int, input().rstrip().split())
  print(check_zero(n, m))