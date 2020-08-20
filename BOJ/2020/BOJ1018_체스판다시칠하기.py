# numpy 사용 못함 - 런타임에러
def min_paint(n, m, board):
    min_nums = []
    for i in range(n-7):
        for j in range(m-7):
            count1, count2 = 0, 0
            for row in range(i, i+8):
                for col in range(j, j+8):
                    if (row+col) % 2 == 0:
                        if board[row][col] != 'W':
                            count1 += 1
                        if board[row][col] != 'B':
                            count2 += 1
                    else:
                        if board[row][col] != 'B':
                            count1 += 1
                        if board[row][col] != 'W':
                            count2 += 1
            min_nums.extend([count1, count2])
    return min(min_nums)


N, M = map(int, input().split())
board = list()
for _ in range(N):
    board.append(list(input()))
print(min_paint(N, M, board))
