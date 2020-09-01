import sys

n = int(sys.stdin.readline())
count = 0
vert, diag, rev_diag = [False]*n, [False]*(2*n-1), [False]*(2*n-1)


def queens(i):
  global count
  # 체스판 모든 행을 돈 경우
  if i == n:
    count += 1
    return
  # 아닌 경우 해당 행의 모든 열 루프
  for j in range(n):
    # 상하, 왼쪽/오른쪽 대각선 모두 퀸이 없는 경우
    if not(vert[j] or diag[i+j] or rev_diag[i-j+n-1]):
      # 해당 행의 열에 퀸 위치 고정
      vert[j] = diag[i+j] = rev_diag[i-j+n-1] = True
      # 다음 행으로 이동
      queens(i+1)
      # 다시 초기화
      vert[j] = diag[i+j] = rev_diag[i-j+n-1] = False


queens(0)
print(count)