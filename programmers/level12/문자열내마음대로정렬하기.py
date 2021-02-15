def solution(strings, n):
    strings = sorted(sorted(strings), key=lambda x:x[n])
    return strings