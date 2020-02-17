tc = list(map(int, input().split()))
K, N, M = tc[0], tc[1], tc[2]
rt = (K*N) - M

if rt <= 0:
    print(0)
else:
    print(rt)
