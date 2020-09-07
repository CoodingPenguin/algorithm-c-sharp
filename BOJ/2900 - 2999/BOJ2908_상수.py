def reverse_num(x):
    x = x[::-1]
    return int(x)

nums = list(map(reverse_num, input().split()))
print(max(nums))
