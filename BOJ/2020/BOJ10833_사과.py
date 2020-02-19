N = int(input())
rt = 0

for n in range(N):
    apps = list(map(int, input().split()))
    rt += apps[1] % apps[0]

print(rt)
