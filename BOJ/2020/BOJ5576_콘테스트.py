w, k = list(), list()
for _ in range(10):
    w.append(int(input()))
for _ in range(10):
    k.append(int(input()))
w, k = sorted(w), sorted(k)
print(sum(w[-3:]), sum(k[-3:]))
