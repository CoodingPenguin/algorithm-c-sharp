def solution(s):
    length = len(s)
    if length%2:
        return s[length//2]
    return s[length//2-1: length//2+1]