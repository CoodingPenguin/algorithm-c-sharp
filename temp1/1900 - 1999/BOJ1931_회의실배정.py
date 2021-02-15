import sys

input = sys.stdin.readline

def result(scheds):
  count = 0
  end = 0
  for i in range(len(scheds)):
    if end <= scheds[i][0]:
      end = scheds[i][1]
      count += 1
  return count


if __name__ == "__main__":
  n = int(input())
  scheds = list()
  for _ in range(n):
    start, end = map(int, input().split())
    scheds.append((start, end))
  scheds.sort(key=lambda x:(x[1], x[0]))
  print(result(scheds))