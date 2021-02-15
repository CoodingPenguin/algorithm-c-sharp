def solution(arr1, arr2):
    (N, M) = (len(arr1), len(arr1[0]))
    answer = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer
