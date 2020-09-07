def result(num):
    if num < 100:
        return num
    cnt = 99
    for n in range(100, num+1):
        digits = [int(digit) for digit in str(n)]
        if (digits[0] - digits[1]) == (digits[1] - digits[2]):
            cnt += 1
    return cnt


N = int(input())
print(result(N))
