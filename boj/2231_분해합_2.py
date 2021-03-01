def smallest_cons(n):
    minRange = n - len(str(n)) * 9
    minRange = 1 if minRange < 1 else minRange
    for i in range(minRange, n):
        decom = i + sum(map(int, list(str(i))))
        if decom == n:
            return i
    return 0


N = int(input())
print(smallest_cons(N))
