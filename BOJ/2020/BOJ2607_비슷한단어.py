def result(t, cs):
    rt = 0
    for c in cs:
        if t == c: rt += 1; continue;
        # 하나를 더하거나
        for ta, ca in t, c:
            
        # 하나를 빼거나
        # 하나의 문자를 다른 문자로 바꾸면



N = int(input())
target = sorted(input())
candidates = []
for _ in range(N-1):
    candidates.append(sorted(input()))

print(result(target, candidates))