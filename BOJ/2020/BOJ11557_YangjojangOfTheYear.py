T = int(input())

for t in range(T):
    N = int(input())
    ss = {}
    for n in range(N):
        s = list(input().split())
        ss[s[0]] = int(s[1])

    print(max(ss.keys(), key=ss.get))
