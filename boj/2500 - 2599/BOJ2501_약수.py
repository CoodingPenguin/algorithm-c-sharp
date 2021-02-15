def my_factors(n):
    factors = [1, n]
    for i in range(2, n//2+1):
        if n % i == 0:
            factors.append(i)

    return sorted(factors)


ls = list(map(int, input().split()))
N, K = ls[0], ls[1]
myFactors = my_factors(N)
if len(myFactors) < K:
    print(0)
else:
    print(myFactors[K-1])
