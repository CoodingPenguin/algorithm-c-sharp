def result(ai, k):
    rt = 0
    for a in ai[::-1]:
        if a <= k:
            rt += k // a
            k %= a

    return rt


_ = list(map(int, input().split()))
N, K = _[0], _[1]
ai = list()
for n in range(N):
    ai.append(int(input()))
print(result(ai, K))
