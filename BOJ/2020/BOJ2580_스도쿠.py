import sys


def row_check(row, value):
    if value in board[row]:
        return False
    return True


def col_check(col, value):
    for _ in range(9):
        if value == board[_][col]:
            return False
    return True


def group_check(row, col, value):
    from_row = row//3 * 3
    from_col = col//3 * 3
    for i in range(3):
        for j in range(3):
            if value == board[from_row+i][from_col+j]:
                return False
    return True


def sudoku(idx):
    if idx == len(blanks):
        for row in board:
            print(' '.join(map(str, row)))
        sys.exit()
    else:
        for val in range(1, 10):
            idx_x = blanks[idx][0]
            idx_y = blanks[idx][1]

            if row_check(idx_x, val) and col_check(idx_y, val) and group_check(idx_x, idx_y, val):
                board[idx_x][idx_y] = val
                sudoku(idx+1)
                board[idx_x][idx_y] = 0


board = list()
for _ in range(9):
    board.append(list(map(int, input().split())))
blanks = list()
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blanks.append((i, j))
sudoku(0)
