n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0
# 현재 그룹에 포함된 모험가의 수 ≥ 현재 확인하고 있는 공포도
# 하나의 그룹으로 묶는다
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)