def result(a, b, c):
    if b == c:
        return -1
    rt = a//(c-b)
    if rt < 0:
        return -1
    return rt+1


A, B, C = map(int, input().split())
print(result(A, B, C))
