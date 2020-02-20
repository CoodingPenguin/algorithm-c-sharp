def result(nums, n):
    dpTable = [0]*n
    dpTable[0] = nums[0]

    for i in range(1, n):
        if dpTable[i-1]+nums[i] > nums[i]:
            dpTable[i] = dpTable[i-1]+nums[i]
        else:
            dpTable[i] = nums[i]

    return max(dpTable)


N = int(input())
nums = list(map(int, input().split()))
print(result(nums, N))
