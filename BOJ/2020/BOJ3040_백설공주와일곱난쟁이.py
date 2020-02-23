def result(ns):
    for i in range(9):
        for j in range(i+1, 9):
            if sum(ns) - ns[i] - ns[j] == 100:
                return i, j


ns = list()
for _ in range(9):
    ns.append(int(input()))
ns = sorted(ns)
i, j = result(ns)
for idx, n in enumerate(ns):
    if idx != i and idx != j:
        print(n)
