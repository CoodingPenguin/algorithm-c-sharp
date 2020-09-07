W = input()
V = ['a', 'e', 'i', 'o', 'u']
rt = 0
for v in V:
    rt += W.count(v)
print(rt)
