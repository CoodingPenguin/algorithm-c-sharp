round = int(input())

sx, sy = 100, 100
for r in range(round):
    dices = list(map(int, input().split()))

    if dices[0] > dices[1]:
        sy -= dices[0]
    elif dices[0] < dices[1]:
        sx -= dices[1]

print(sx)
print(sy)
