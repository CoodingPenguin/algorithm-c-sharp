from math import gcd

n = int(input())
rings = list(map(int, input().split()))

for ring in rings[1:]:
  g = gcd(rings[0], ring)
  print(f'{rings[0]//g}/{ring//g}')
