def gcd(n, m):
    while m > 0:
        q = n//m
        r = n-q*m
        n, m = m, r
    return n


def solution(n, m):
    GCD = gcd(n, m)
    GCM = n*m//GCD
    return [GCD, GCM]
