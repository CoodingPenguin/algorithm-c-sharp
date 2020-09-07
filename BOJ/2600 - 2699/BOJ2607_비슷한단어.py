def result(target, candidates):
    rt = 0
    for candidate in candidates:
        diff = len(target) - len(candidate)
        for t in target:
            if t in candidate:
                candidate.remove(t)
        rest = len(candidate)
        if (diff == 0 and (rest == 0 or rest == 1)) or (diff == 1 and rest == 0) or (diff == -1 and rest == 1):
            rt += 1

    return rt


N = int(input())
target = list(input())
candidates = []
for _ in range(N-1):
    candidates.append(list(input()))

print(result(target, candidates))
