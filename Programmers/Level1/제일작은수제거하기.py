def solution(arr):
    arr.remove(min(arr))
    if not arr:
        return [-1]
    return arr