N = int(input())
nums = list(filter(lambda x: '666' in str(x), range(666, 3000000)))
print(nums[N-1])
