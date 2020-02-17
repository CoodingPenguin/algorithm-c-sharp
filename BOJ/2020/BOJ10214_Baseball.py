def result(scores):
    yw, kw = sum([s[0] for s in scores]), sum([s[1] for s in scores])
    if yw > kw:
        return "Yonsei"
    elif yw < kw:
        return "Korea"
    else:
        return "Draw"


T = int(input())

for t in range(T):
    scores = []
    for g in range(9):
        scores.append(list(map(int, input().split())))
    print(result(scores))
