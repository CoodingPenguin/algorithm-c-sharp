import sys

N = int(sys.stdin.readline())
rgb = [[0, 0, 0]]

for _ in range(N):
  r, g, b = map(int, sys.stdin.readline().split())
  new_r = r + min(rgb[-1][1], rgb[-1][2])
  new_g = g + min(rgb[-1][0], rgb[-1][2])
  new_b = b + min(rgb[-1][0], rgb[-1][1])
  rgb.append([new_r, new_g, new_b])

print(min(rgb[N]))