def solution(arr):
    result = []
    for element in arr:
        if not result:
            result.append(element)
        else:
            if result[-1] != element:
                result.append(element)
    return result