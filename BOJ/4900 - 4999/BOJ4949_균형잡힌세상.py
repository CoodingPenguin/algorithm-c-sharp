import sys


def check_balance(line):
  stack = []
  for letter in line:
    if letter in ("(", "["):
      stack.append(letter)
    elif letter in (")", "]"):
      try:
        top = stack.pop()
        if not top+letter in ("()", "[]"):
          stack.extend([top, letter])
      except:
        return "no"
  if not stack:
    return "yes"
  return "no"


if __name__ == "__main__":
  for line in sys.stdin:
    line = line.rstrip()
    if line == ".":
      break
    print(check_balance(line))