rec = list()
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        rec.pop()
    else:
        rec.append(n)
print(sum(rec))
