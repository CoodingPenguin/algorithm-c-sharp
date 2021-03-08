import sys

input = sys.stdin.readline


def check_same(x, y, size):
    pred = arr[x][y]
    for i in range(size):
        for j in range(size):
            if arr[x + i][y + j] != pred:
                return False, None
    return True, pred


def cut_paper(x, y, size):
    if size == 0:
        return
    # 1. 종이의 모든 숫자가 같은 수인지 확인한다.
    is_same, pred = check_same(x, y, size)
    # 2. 만약 같다면 해당 숫자의 카운트를 증가시킨다.
    if is_same:
        counts[pred] += 1
    # 3. 아니라면 종이를 다시 3*3으로 자른다.
    else:
        new_size = size // 3
        for i in range(0, size, new_size):
            for j in range(0, size, new_size):
                cut_paper(x + i, y + j, new_size)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
counts = [0] * 3
cut_paper(0, 0, N)
for i in [-1, 0, 1]:
    print(counts[i])

