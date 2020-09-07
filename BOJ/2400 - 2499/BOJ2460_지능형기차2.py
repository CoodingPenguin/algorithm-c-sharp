rt = 0
pt = 0
for _ in range(10):
    cinout = list(map(int, input().split()))
    pt += cinout[1] - cinout[0]
    if pt > rt:
        rt = pt

print(rt)
