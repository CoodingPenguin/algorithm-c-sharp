import sys

input = sys.stdin.readline

# 입력
K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

result = 0
start, end = 1, max(lines)
while start <= end:
    mid = (start + end) // 2
    num_of_lines = sum([line // mid for line in lines])
    if num_of_lines < N:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

# 출력
print(result)
