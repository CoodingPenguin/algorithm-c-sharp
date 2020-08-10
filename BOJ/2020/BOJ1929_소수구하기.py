# 참고 : https://wlstyql.tistory.com/73
def result(m, n):
    n += 1
    primeNumber = [True]*n
    for i in range(2, int(n**0.5)+1):
        if primeNumber[i]:
            for j in range(2*i, n, i):
                primeNumber[j] = False

    for i in range(m, n):
        if i > 1:
            if primeNumber[i]:
                print(i)


M, N = map(int, input().split())
result(M, N)
