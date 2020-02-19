N = int(input())
for n in range(N):
    P = int(input())
    players = {}

    for p in range(P):
        player = list(input().split())
        players[player[1]] = int(player[0])

    print(max(players, key=players.get))
