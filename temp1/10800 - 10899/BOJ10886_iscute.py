def is_cute(v):
    if v == 1:
        return "Junhee is cute!"
    else:
        return "Junhee is not cute!"


def result(vs, n):
    if len(vs) == 1:
        return is_cute(vs[0])

    vs = sorted(vs)
    idx = n//2
    return is_cute(vs[idx])


N = int(input())
vs = []

for n in range(N):
    vs.append(int(input()))

print(result(vs, N))
