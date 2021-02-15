def least_common_mult(x,  y):
    if x == 1:
        return y
    if x == 2 and y % 2 == 0:
        return y

    i, j = 1, 1
    while True:
        if x*i == y*j:
            return x*i
        elif x*i > y*j:
            j += 1
        else:
            i += 1


T = int(input())
for t in range(T):
    nums = sorted(list(map(int, input().split())))
    x, y = nums[0], nums[1]
    print(least_common_mult(x, y))
