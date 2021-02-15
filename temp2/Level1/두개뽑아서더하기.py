from itertools import combinations

def solution(numbers):
    result = [sum(comb) for comb in combinations(numbers, 2)]
    result = sorted(list(set(result)))
    return result