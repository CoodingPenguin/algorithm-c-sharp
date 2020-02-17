while True:
    tc = list(map(int, input().split()))
    x, y = tc[0], tc[1]

    if x == 0 and y == 0:
        break

    if x > y:
        print("Yes")
    else:
        print("No")
