def solution(num):
    for i in range(1, 501):
        num = num*3+1 if num%2 else num//2
        if num == 1:
            return i
    return -1