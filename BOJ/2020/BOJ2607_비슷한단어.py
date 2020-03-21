def result(t, cs):
    rt = 0
    for c in cs:
        if c == t:
            print(f"Case #1  : {c}")
            rt += 1
        # 하나를 더하거나
        elif len(c) == len(t) + 1 and set(c).issuperset(set(t)):
            print(f"Case #2  : {c}")
            rt += 1
        # 하나를 빼거나
        elif len(c) == len(t) - 1 and set(c).issubset(set(t)):
            print(f"Case #3  : {c}")
            rt += 1
        # 하나의 문자를 다른 문자로 바꾸면
        else:
            if len(c) == len(t):
                stack = t.copy()
                for i in range(len(c)):
                    try:
                        stack.remove(c[i])
                    except:
                        pass
                if len(stack) == 1:
                    print(f"Case #4 : {c}")
                    rt += 1

    return rt


N = int(input())
target = sorted(input())
candidates = []
for _ in range(N-1):
    candidates.append(sorted(input()))

print(result(target, candidates))
