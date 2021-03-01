import sys


input = sys.stdin.readline

# 명령어 로그도 기록하는 Stack 클래스
class Stack:
  def __init__(self):
    self.stack = []     # 스택
    self.commands = []  # 명령어
  
  def __len__(self):
    return len(self.stack)
  
  def append(self, n):
    self.stack.append(n)
    self.commands.append("+")
  
  def pop(self):
    self.stack.pop()
    self.commands.append("-")

  def top(self):
    if self.stack:
      return self.stack[-1]
    return None

  def get_commands(self):
    return self.commands


def create_commands(n, series):
  stack = Stack()
  item, point = 1, 0  # stack 요소, 수열 포인터

  while item <= n:
    # 스택의 top과 현재 수열 요소가 같은 경우 스택에서 해당 요소를 꺼낸다
    if stack.top() == series[point]:
      stack.pop()
      point += 1
    # 다른 경우 요소를 넣는다
    else:
      stack.append(item)
      item += 1
  
  # 남은 수열 요소도 똑같이 검사
  while point < n:
    if stack.top() == series[point]:
      stack.pop()
    point += 1

  # 스택이 비어있고 모든 수열을 돌았다면 명령어 로그 반환
  if not len(stack) and point == n:
    return stack.get_commands()
  return None  


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