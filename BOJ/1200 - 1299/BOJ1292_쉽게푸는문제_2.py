# 풀이 2
n = []

for i in range(1, 46):
    for j in range(1, i+1):
        n.append(i)


_ = list(map(int, input().split()))
s, e = _[0], _[1]
print(sum(n[s-1:e]))
