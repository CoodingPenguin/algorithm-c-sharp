def result(scores):
    sortedOne = list(sorted(scores))[3:]
    idx = []
    for i, s in enumerate(scores):
        if s in sortedOne:
            idx.append(i)

    print(sum(sortedOne))
    for i in idx:
        print(i+1, end=" ")


scores = []
for _ in range(8):
    scores.append(int(input()))
result(scores)
