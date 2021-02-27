ns = list()
for _ in range(5):
    ns.append(int(input()))
ns = sorted(ns)
print(sum(ns) // len(ns))
print(ns[2])
