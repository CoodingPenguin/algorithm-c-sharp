import sys

input = sys.stdin.readline


def check_all_same(arr, n):
    digit = arr[0][0]
    if n == 1:
        return digit
    for i in range(n):
        for j in range(n):
            if arr[i][j] is not digit:
                return False
    return digit


def zip_arr(arr, n):
    check = check_all_same(arr, n)
    if check:
        return [check]
    else:
        up_left = [row[0 : n // 2] for row in arr[0 : n // 2]]
        up_right = [row[n // 2 : n] for row in arr[0 : n // 2]]
        down_left = [row[0 : n // 2] for row in arr[n // 2 : n]]
        down_right = [row[n // 2 : n] for row in arr[n // 2 : n]]
        sub_arr = [up_left, up_right, down_left, down_right]

        result = []
        for s_arr in sub_arr:
            check = check_all_same(s_arr, n // 2)
            if check:
                result.append(check)
            else:
                result.append(zip_arr(s_arr, n // 2))
        return result


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
result = zip_arr(arr, N)
if len(result) < 2:
    print(result.pop())
else:
    result = str(result)
    result = result.replace("'", "").replace(", ", "")
    result = result.replace("[", "(").replace("]", ")")
    print(result)

