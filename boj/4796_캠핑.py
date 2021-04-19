import sys

input = sys.stdin.readline
count = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    result = (V // P) * L
    result += L if V % P > L else V % P
    print(f"Case {count}: {result}")
    count += 1

