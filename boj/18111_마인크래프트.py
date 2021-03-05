import sys
from collections import Counter

input = sys.stdin.readline


def calculate_time(base):
    total_time = 0
    for height in blocks:
        # base보다 작으면 블럭을 채운다.
        if height < base:
            total_time += (base - height) * blocks[height]
        # base보다 크면 블럭을 깎는다.
        elif height > base:
            total_time += 2 * (height - base) * blocks[height]
    return total_time


# 입력
N, M, B = map(int, input().split())
blocks = []
for _ in range(N):
    blocks.extend(map(int, input().split()))

sum_of_blocks, len_of_blocks = sum(blocks), N * M
blocks = Counter(blocks)
result_time, result_height = 1e20, 0

for base in range(257):
    # 맞추고자 하는 블럭 수가 현재 마련된 블럭수 보다 작을 경우에만 실행
    if len_of_blocks * base <= sum_of_blocks + B:
        total_time = calculate_time(base)
        if total_time <= result_time:
            result_time = total_time
            result_height = base

# 출력
print(result_time, result_height)
