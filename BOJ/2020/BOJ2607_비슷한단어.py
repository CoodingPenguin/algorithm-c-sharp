def result(t, cs):
    rt = 0
    for c in cs:
        if c == t:
            rt += 1
            continue
        # 하나를 더하거나
        if len(c) == len(t) + 1:
            for i in range(len(t)):
                if c[i] != t[i]:
                    break

        # 하나를 빼거나
        # 하나의 문자를 다른 문자로 바꾸면


N = int(input())
target = sorted(input())
candidates = []
for _ in range(N-1):
    candidates.append(sorted(input()))

print(result(target, candidates))
