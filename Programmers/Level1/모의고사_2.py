from itertools import cycle


def solution(answers):
    # 수포자 패턴
    people = [
        cycle([1, 2, 3, 4, 5]),
        cycle([2, 1, 2, 3, 2, 4, 2, 5]),
        cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]),
    ]
    totalScore = [0, 0, 0]    # 최종 점수
    # 채점
    for ans in answers:
        for idx, aList in enumerate(people):
            if next(aList) == ans:
                totalScore[idx] += 1
    maxScore = max(totalScore)  # 최고점

    return [idx+1 for idx, score in enumerate(totalScore) if score == maxScore]
