def isAdvertise(r, e, c):
    if r < e-c:
        return "advertise"
    elif r > e-c:
        return "do not advertise"
    else:
        return "does not matter"


TC = int(input())

for t in range(TC):
    params = list(map(int, input().split()))
    r, e, c = params[0], params[1], params[2]
    print(isAdvertise(r, e, c))
