import sys

coords = []
for _ in range(int(sys.stdin.readline())):
  x, y = map(int, sys.stdin.readline().split())
  coords.append((x, y))

coords = sorted(coords, key=lambda x:x[::-1])
for x, y in coords:
  print(x, y)