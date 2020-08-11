def result(N):
    start, end = N+1, 2*N+1
    primeNum = [True] * end
    for i in range(2, end):
        if primeNum[i]:
            for j in range(2*i, end, i):
                primeNum[j] = False
    return sum(primeNum[start:])


while True:
    N = int(input())
    if N == 0:
        break
    result(N)
