import sys

def queens(i):
  global count
  # 모든 행을 다 돌았을 때
  if i == N:
    count += 1
  # 다 돌지 못한 경우
  else:
    #해당 행의 열을 탐색
    for j in range(N):
      col[i] = j
      if promising(i):
        queens(i+1)

def promising(i):
  for k in range(i):
    # 같은 열 혹은 같은 대각선에 있는 경우
    if (col[i] == col[k]) or (abs(col[i]-col[k])==i-k):
      return False
  return True

N = int(sys.stdin.readline())
col = [0]*N
count = 0
queens(0)
print(count)