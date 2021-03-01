import sys

# 가로축 검사
def row_check(row, value):
  if value in board[row]:
    return False
  return True

# 세로축 검사
def col_check(col, value):
  for _ in range(9):
    if value == board[_][col]:
      return False
  return True

# 3*3 그룹 검사
def group_check(row, col, value):
  from_row = row//3 * 3
  from_col = col//3 * 3
  for i in range(3):
    for j in range(3):
      if value == board[from_row+i][from_col+j]:
        return False
  return True


def sudoku(idx):
  # 모두 채웠다면 출력 및 종료
  if idx == len(blanks):
    for row in board:
      print(' '.join(map(str, row)))
    sys.exit()
  else:
    # 1-9의 값을 하나씩 넣어보며 검사
    for val in range(1, 10):
      # 빈 칸의 위치
      idx_x = blanks[idx][0]
      idx_y = blanks[idx][1]

      # 해당 값으로 채워도 문제가 없다면
      if row_check(idx_x, val) and col_check(idx_y, val) and group_check(idx_x, idx_y, val):
        # 해당 값으로 채우기
        board[idx_x][idx_y] = val
        # 다음 빈칸으로 이동
        sudoku(idx+1)
        # 다시 돌아올 것에 대비해 초기화
        board[idx_x][idx_y] = 0  


board = list()
for _ in range(9):
  board.append(list(map(int, input().split())))
# 빈칸의 위치 저장
blanks = list()
for i in range(9):
  for j in range(9):
    if board[i][j] == 0:
      blanks.append((i, j))
sudoku(0)
