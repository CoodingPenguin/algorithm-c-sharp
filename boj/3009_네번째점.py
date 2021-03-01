def result(points):
    xs = sorted([point[0] for point in points])
    ys = sorted([point[1] for point in points])
    rtx, rty = 0, 0

    if xs[0] == xs[1]:
        rtx = xs[2]
    else:
        rtx = xs[0]

    if ys[0] == ys[1]:
        rty = ys[2]
    else:
        rty = ys[0]

    print(rtx, rty)


points = []
for i in range(3):
    point = list(map(int, input().split()))
    points.append(point)

result(points)
