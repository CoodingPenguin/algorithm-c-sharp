def solution(n):
    if n in (0, 1):
        return n
    result = 1+n
    for num in range(2, n//2+1):
        if n % num == 0:
            result += num
    return result
