# 참고 :  https://www.acmicpc.net/source/21902130
N = int(input())
cnt, num = 0, 665
while cnt < N:
    num += 1
    if '666' in str(num):
        cnt += 1

print(num)
