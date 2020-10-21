from collections import namedtuple

# 입력
n, k = map(int, input().split())
Stuff = namedtuple('Stuff', 'weight value')
lst = [Stuff(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    stuff = Stuff(weight=w, value=v)
    lst.append(stuff)
lst.sort()


# 테이블 채우기
table = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    # 현재 넣으려 하는 물건의 무게와 가치
    w, v = lst[i].weight, lst[i].value
    for j in range(1, k+1):
        # 현재 가능한 무게 j보다 무게가 작을 때 = 넣을 수 있음
        if w <= j:
            # 두 케이스 비교
            # 1. i-1개, j-w만큼 넣을 수 있을 때의 가치합 + 현재 물건의 가치
            # 2. i-1개, j만큼 넣을 수 있을 때의 가치합
            if v + table[i-1][j-w] > table[i-1][j]:
                # 케이스 1. 갱신
                table[i][j] = v + table[i-1][j-w]
            else:
                # 케이스 2. 그대로
                table[i][j] = table[i-1][j]
        # 현재 가능한 무게 j보다 무게가 클 때 = 못 넣음
        # 그 전의 가치합의 최대값을 그대로 가져옴
        else:
            table[i][j] = table[i-1][j]

print(table[n][k])
