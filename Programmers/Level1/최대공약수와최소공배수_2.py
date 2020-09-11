def solution(n, m):
    def gcd(a, b): return b if not a % b else gcd(b, a % b)
    def lcm(a, b): return a*b//gcd(a, b)
    return [gcd(n, m), lcm(n, m)]
