import sys


input = sys.stdin.readline

def create_commands(n, series):
  stack, commands = [], []
  item = 0

  for target in series:
    # target을 만날 때까지 스택에 push
    while item < target:
      item += 1
      stack.append(item)
      commands.append('+')
    # target을 만나면 스택에서 pop
    if target == stack[-1]:
      stack.pop()
      commands.append('-')
    # target을 만나지 못한 경우는 만들 수 없으므로  None 반환
    else:
      return None
  return commands


if __name__ == "__main__":
  n = int(input().rstrip())
  series = []
  for _ in range(n):
    series.append(int(input()))
  
  commands = create_commands(n, series)
  if not commands:
    print("NO")
  else:
    for c in commands:
      print(c) 