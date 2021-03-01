N, ts = int(input()), list(map(int, input().split()))
rt = list()
for i in range(N):
    rt.insert(i-ts[i], i+1)
print(' '.join(map(str, rt)))
