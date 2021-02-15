import sys

input = sys.stdin.readline

def parse(expr):
  stack = [int(expr[0]) if expr[0].isdigit() else expr[0]]
  for letter in expr[1:]:
    item = stack.pop()
    if letter.isdigit():
      letter = int(letter)
      if isinstance(item, int):
        stack.append(item*10+letter)
        continue
    stack.extend([item, letter])
  return stack


def result(expr):
  stack = parse(expr)
  total = stack[0]
  is_minus = False
  for item in stack[1:]:
    if item == "-":
      is_minus = True
    if isinstance(item, int):
      if is_minus:
        total -= item
      else:
        total += item
  return total
    

if __name__ == "__main__":
  expr = input().strip()
  print(result(expr))