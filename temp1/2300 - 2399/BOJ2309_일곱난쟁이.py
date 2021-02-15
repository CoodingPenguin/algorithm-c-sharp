def result(hs):
    for i in range(9):
        for j in range(i+1, 9):
            if sum(hs) - hs[i] - hs[j] == 100:
                return i, j


hs = []
for _ in range(9):
    hs.append(int(input()))
hs = sorted(hs)
i, j = result(hs)
for idx, h in enumerate(hs):
    if idx == i or idx == j:
        continue
    print(h)
