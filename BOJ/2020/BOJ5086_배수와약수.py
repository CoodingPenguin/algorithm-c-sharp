def result(x, y):
    if x < y and y % x == 0:
        return "factor"
    elif x > y and x % y == 0:
        return "multiple"
    else:
        return "neither"


while True:
    nums = list(map(int, input().split()))
    x, y = nums[0], nums[1]

    if x == 0 and y == 0:
        break
    print(result(x, y))
