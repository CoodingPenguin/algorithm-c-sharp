# 출처: https://www.acmicpc.net/source/17969385
N = int(input())
count = [0]*2
for i in range(N, 0, -1):
    while i % 2 == 0:
        count[0] += 1
        i = i//2
    while i % 5 == 0:
        count[1] += 1
        i = i//5
print(min(count))
