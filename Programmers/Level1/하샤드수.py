def solution(x):
    if x%sum(map(int, list(str(x)))):
        return False
    return True