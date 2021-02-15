from collections import deque
import sys

input = sys.stdin.readline

class Queue:
  def __init__(self):
    self.dq = deque()

  def push(self, item):
    self.dq.append(item)
  
  def pop(self):
    if self.dq:
      item = self.dq.popleft()
      return item
    return -1
    
  def size(self):
    return len(self.dq)
  
  def empty(self):
    if not self.dq:
      return 1
    return 0
  
  def front(self):
    if self.dq:
      return self.dq[0]
    return -1
  
  def back(self):
    if self.dq:
      return self.dq[-1]
    return -1


if __name__ == "__main__":
  n = int(input().rstrip())
  queue = Queue()

  for _ in range(n):
    command_item = input().rstrip().split()
    command = command_item[0]
    item = None
    if len(command_item) > 1:
      item = int(command_item[1])
    
    if command == "push":
      queue.push(item)
    elif command == "pop":
      print(queue.pop())
    elif command == "size":
      print(queue.size())
    elif command == "empty":
      print(queue.empty())
    elif command == "front":
      print(queue.front())
    else:
      print(queue.back())

