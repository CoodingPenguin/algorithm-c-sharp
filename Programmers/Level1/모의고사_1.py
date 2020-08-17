def solution(answers):
    # 수포자 패턴
    result = []
    n = len(answers)
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 채점
    p1 = sum([True if p1[i % 5] == answers[i] else False for i in range(n)])
    p2 = sum([True if p2[i % 8] == answers[i] else False for i in range(n)])
    p3 = sum([True if p3[i % 10] == answers[i] else False for i in range(n)])

    # 높은 순으로 정렬
    total = [p1, p2, p3]
    maxScore = max(total)
    for p, s in enumerate(total):
        if total[p] == maxScore:
            result.append(p+1)
    return result
