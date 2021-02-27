def fibb(n):
    fibNums = [0, 1]
    for i in range(2, n+1):
        fibNums.append(fibNums[i-2]+fibNums[i-1])
    return fibNums[n]


N = int(input())
print(fibb(N))
