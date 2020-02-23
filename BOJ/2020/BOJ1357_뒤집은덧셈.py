def rev(n):
    return int(str(n)[::-1])


_ = list(map(int, input().split()))
x, y = _[0], _[1]
print(rev(rev(x) + rev(y)))
