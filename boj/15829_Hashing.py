import sys
from collections import deque

input = sys.stdin.readline

R = 31
M = 1234567891
L = int(input())

chars = input().rstrip()
ords = [ord(char) - ord("a") + 1 for char in chars]
h = 0
for i, a in enumerate(ords):
    h += (a * (R ** i)) % M
print(h % M)

