T = int(input())

for t in range(T):
    N = int(input())
    total, grades = 0, 0
    for n in range(N):
        sub = list(map(float, input().split()))
        total += sub[0]*sub[1]
        grades += sub[0]
    print("{0} {1:.1f}".format(int(grades), total/grades))
