def fact(n):
    if n == 1 or n == 0:
        return 1
    return fact(n-1)*n


N = int(input())
print(fact(N))
