def find_all(nums):
    idx = []
    for i in range(len(nums)):
        if i == 0 or i == 1:
            continue
        if nums[i] == False:
            idx.append(i)
    return idx


def gen_prime(m, n):
    prime = [False]*(n+1)
    for i in range(2, n+1):
        if prime[i] == False:
            j = 2
            while i*j <= n:
                prime[i*j] = True
                j += 1

    return list(filter(lambda x: x >= m, find_all(prime)))


M, N = int(input()), int(input())
prime = gen_prime(M, N)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
