rt = {}
for _ in range(5):
    score = sum(list(map(int, input().split())))
    rt[_+1] = score

win = max(rt.keys(), key=rt.get)
print(win, rt[win])
