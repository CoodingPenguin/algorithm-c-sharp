import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
seq = sorted(map(int, input().split()))
acc_sum = [0]
for i in range(len(seq)):
    acc_sum.append(acc_sum[-1] + seq[i])

for _ in range(Q):
    L, R = map(int, input().split())
    print(acc_sum[R] - acc_sum[L - 1])

