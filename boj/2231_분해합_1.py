def smallest_constructor(n):
    length = len(str(n))
    if length == 1:
        return 0
    for i in range(9*(10**(length-2)), n):
        decom = i + sum(map(int, list(str(i))))
        if decom == n:
            return i
    return 0


N = int(input())
print(smallest_constructor(N))
