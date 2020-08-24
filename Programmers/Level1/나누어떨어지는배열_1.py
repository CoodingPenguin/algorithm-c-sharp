def solution(arr, divisor):
    result = list(filter(lambda x:x%divisor==0, arr))
    if not result:
        return [-1]
    return sorted(result)