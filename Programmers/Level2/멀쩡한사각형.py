# 참고: https://leedakyeong.tistory.com/135
import math


def solution(w, h):
    gcd = math.gcd(w, h)
    if gcd == 1:
        return w*h-(w+h-1)
    return w*h-(w+h-gcd)
