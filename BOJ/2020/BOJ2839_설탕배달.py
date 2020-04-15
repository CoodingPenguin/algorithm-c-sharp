def combination(n):
    m = 10000
    for i in range(1, n//3+1):
        r = n-3*i
        if r % 5 == 0:
            k = i+(r//5)
            if k < m:
                m = k
    return m


def result(n):
    p = n//3 if n % 3 == 0 else 10000
    q = n//5 if n % 5 == 0 else 10000
    r = combination(n)

    rt = min(p, q, r)
    if rt == 10000:
        return -1
    return rt


print(result(int(input())))
