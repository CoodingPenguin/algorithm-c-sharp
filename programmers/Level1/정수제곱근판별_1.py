import math

def solution(n):
    if int(math.sqrt(n))**2 == n:
        return int(math.sqrt(n)+1)**2
    return -1