def d(n):
    rt = n
    for digit in str(n):
        rt += int(digit)
    return rt

nums = [False]*10001
for i in range(1, 10000):
    k = d(i)
    if k < 10001:
        nums[k] = True

for idx, v in enumerate(nums):
    if idx == 0:
        continue
    if not v:
        print(idx)