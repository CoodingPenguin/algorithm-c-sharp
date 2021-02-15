def solution(n, arr1, arr2):
    arr = [i | j for i, j in zip(arr1, arr2)]
    result = []
    for target in arr:
        target = str(bin(target))[2:].zfill(n)[-n:]
        target = target.replace('1', '#').replace('0', ' ')
        result.append(target)
    return result
