def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


def result(nums):
    nums = [is_prime(x) for x in nums]
    return nums.count(True)


N = int(input())
nums = sorted(list(map(int, input().split())))
print(result(nums))
