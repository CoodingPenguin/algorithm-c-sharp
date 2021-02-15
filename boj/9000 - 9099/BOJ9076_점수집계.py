def result(scores):
    th = scores[1:4]
    if th[2] - th[0] >= 4:
        return "KIN"
    else:
        return sum(th)


for _ in range(int(input())):
    scores = sorted(list(map(int, input().split())))
    print(result(scores))
