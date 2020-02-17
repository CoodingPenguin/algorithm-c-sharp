def complement(x):
    if x >= 40:
        return x
    else:
        return 40


def result(scores):
    scores = [complement(score) for score in scores]

    return int(sum(scores) / 5)


scores = []
for i in range(5):
    scores.append(int(input()))

print(result(scores))
