while True:
    friends = list(map(int, input().split()))
    xy, xx = friends[0], friends[1]

    if xy == 0 and xx == 0:
        break

    print(xy+xx)
