for _ in range(int(input())):
    ws = input().split()
    wl = len(ws[0])
    dist = [0]*wl
    for idx in range(wl):
        dist[idx] = ord(ws[1][idx]) - ord(ws[0][idx])
        if dist[idx] < 0:
            dist[idx] += 26
    dist = map(str, dist)
    print('Distances: '+' '.join(dist))