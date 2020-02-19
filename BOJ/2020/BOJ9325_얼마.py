T = int(input())

for t in range(T):
    S = int(input())
    N = int(input())
    for n in range(N):
        opt = list(map(int, input().split()))
        S += opt[0] * opt[1]
    print(S)
