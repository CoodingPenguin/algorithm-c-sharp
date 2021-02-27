def calPrize(mydice):
    sorted_dice = sorted(mydice)
    count = len(set(sorted_dice))

    if count == 1:
        return 50000 + sorted_dice[0] * 5000
    elif count == 2:
        if sorted_dice[1] == sorted_dice[2]:
            return 10000 + sorted_dice[1] * 1000
        return 2000 + sorted_dice[1] * 500 + sorted_dice[2]*500
    elif count == 3:
        if sorted_dice[0] == sorted_dice[1] or sorted_dice[1] == sorted_dice[2]:
            return 1000 + sorted_dice[1] * 100
        elif sorted_dice[2] == sorted_dice[3]:
            return 1000 + sorted_dice[2] * 100
    else:
        return max(sorted_dice) * 100


N = int(input())
prizes = []

for n in range(N):
    prize = calPrize([int(x) for x in input().split()])
    prizes.append(prize)


print(max(prizes))
