def solution(n):
    isPrime = [False]*2 + [True]*(n-1)
    for i in range(2, n//2+1):
        if isPrime[i]:
            for j in range(i*2, n+1, i):
                isPrime[j] = False
            
    return sum(isPrime)