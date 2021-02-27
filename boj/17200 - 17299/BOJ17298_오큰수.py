import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
nge = [-1] * N

stack = []
for i in range(N):
    while stack and seq[stack[-1]] < seq[i]:
        nge[stack.pop()] = seq[i]
    stack.append(i)

print(" ".join(map(str, nge)))

