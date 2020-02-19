N = int(input())

for i in range(N):
    print(" "*(N-i-1) + "*" * (2*i+1))
for i in range(N-1, 0, -1):
    print(" "*(N-i) + "*" * (2*i-1))
