import sys

input = sys.stdin.readline

def result(expr):
  sub = list(expr.split('-'))
  total = 0
  for num in sub[0].split('+'):
    total += int(num)
  for num_plus in sub[1:]:
    for num in num_plus.split('+'):
      total -= int(num)
  return total

if __name__ == "__main__":
  expr = input().strip()
  print(result(expr))