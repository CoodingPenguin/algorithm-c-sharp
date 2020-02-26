from functools import reduce
N = int(input())
if N == 0:
    fact = "1"
else:
    fact = str(reduce(lambda x, y: x*y, range(1, N+1)))[::-1]
rt = 0
while fact[rt] == "0":
    rt += 1
print(rt)
