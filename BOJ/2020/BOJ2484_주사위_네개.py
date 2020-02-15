def calPrize(mydice):
    sorted_dice = mydice.sort()
    count = len(set(sorted_dice))

    if count == 1:
        return 50000 + sorted_dice[0] * 5000
    elif count == 2:
        if sorted_dice[1] == sorted_dice[2]:
            return 10000 + sorted_dice[1] * 1000
        return sorted_dice[1] * 500 + sorted_dice[2]*500
    

    

ppl = int(input())
dice = []

for p in range(ppl):
    lst = [int(x) for x in input().split()]
    dice.append(lst)


