def result(p, m, v):
    if m == 1:
        return p-1
    return len(v) - len(set(v))


for _ in range(int(input())):
    i = list(map(int, input().split()))
    p, m = i[0], i[1]
    v = []
    for __ in range(p):
        v.append(int(input()))
    print(result(p, m, v))
