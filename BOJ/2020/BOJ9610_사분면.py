def result(coords):
    q1, q2, q3, q4, axis = 0, 0, 0, 0, 0

    for c in coords:
        if c[0] == 0 or c[1] == 0:
            axis += 1
        elif c[0] > 0:
            if c[1] > 0:
                q1 += 1
            else:
                q4 += 1
        else:
            if c[1] > 0:
                q2 += 1
            else:
                q3 += 1

    print("Q1: {0}\nQ2: {1}\nQ3: {2}\nQ4: {3}\nAXIS: {4}".format(
        q1, q2, q3, q4, axis))


tc = int(input())
coords = []

for t in range(tc):
    coords.append(list(map(int, input().split())))
result(coords)
