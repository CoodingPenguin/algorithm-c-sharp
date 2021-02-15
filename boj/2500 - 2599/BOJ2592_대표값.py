def mode(ns):
    nss = list(set(ns))
    count = {}
    for n in nss:
        count[n] = ns.count(n)
    return max(count.keys(), key=count.get)


def average(ns):
    return int(sum(ns) / len(ns))


ns = []
for _ in range(10):
    ns.append(int(input()))
print(average(ns))
print(mode(ns))
