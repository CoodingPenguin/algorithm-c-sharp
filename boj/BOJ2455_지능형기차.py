mp, pp = 0, 0

for _ in range(4):
    sub = list(map(int, input().split()))
    pp += sub[1] - sub[0]
    if mp < pp:
        mp = pp
print(mp)
