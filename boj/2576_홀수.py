def func(x):
    if x % 2 == 1:
        return x
    else:
        return None


nums = []
for _ in range(7):
    nums.append(int(input()))

odds = list(filter(func, nums))
if len(odds) == 0:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))
