def result(N):
    # 에라토스테네스의 체
    isPrime = [False] * 2 + [True] * (N-2)
    for i in range(2, int(N/2)):
        if isPrime[i]:
            for j in range(2*i, N, i):
                isPrime[j] = False

    # 최대 파티션 검사
    minPrime, maxPrime = 0, 0
    for i in range(2, int(N/2+1)):
        num1, num2 = i, N-i
        if isPrime[num1] and isPrime[num2]:
            minPrime, maxPrime = num1, num2

    return minPrime, maxPrime


for _ in range(int(input())):
    minPrime, maxPrime = result(int(input()))
    print(minPrime, maxPrime)
