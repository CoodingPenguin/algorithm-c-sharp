def result(n):
    m = 1
    while n > 0:
        n -= m
        m += 1
    if m % 2 == 0:
        return f"{1-n}/{m+n-1}"
    else:
        return f"{m+n-1}/{1-n}"


N = int(input())
print(result(N))
