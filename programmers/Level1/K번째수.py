def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        arr = array[i-1:j]
        answer.append(sorted(arr)[k-1])
    return answer
