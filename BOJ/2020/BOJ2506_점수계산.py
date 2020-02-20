def score(test):
    rt, acc = 0, 0
    for i in range(len(test)):
        if test[i] == 1:
            rt += test[i] + acc
            acc += 1
        else:
            acc = 0
    return rt


N = int(input())
test = list(map(int, input().split()))

print(score(test))
