def cal_prize(dices):
    dices = sorted(dices)
    count = len(set(dices))

    if count == 1:
        return 10000+dices[0]*1000
    elif count == 2:
        return 1000 + dices[1]*100
    else:
        return max(dices)*100


tc = list(map(int, input().split()))
print(cal_prize(tc))
