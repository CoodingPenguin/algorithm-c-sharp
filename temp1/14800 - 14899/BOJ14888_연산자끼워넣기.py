from itertools import permutations

# 입력
n = int(input())
operands = list(map(int, input().split()))
raws = list(map(int, input().split()))
operators = list()
for operator, number in enumerate(raws):
    operators.extend([operator]*number)
operatorsList = list(set(permutations(operators)))

# 출력
MIN = MAX = 0
for i, operators in enumerate(operatorsList):
    result = operands[0]
    for operand, operator in zip(operands[1:], operators):
        if operator == 0:
            result += operand
        elif operator == 1:
            result -= operand
        elif operator == 2:
            result *= operand
        else:
            result /= operand
            result = int(result)
    if i == 0:
        MIN = MAX = result
    MIN = min(result, MIN)
    MAX = max(result, MAX)

print(MAX)
print(MIN)
