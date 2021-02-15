def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        # 선행 스킬 순서
        skill_list = list(skill)

        for s in skills:
            # 만약 해당 스킬이 선행 스킬에 있는 스킬이라면
            # 가장 앞의 선행 스킬을 꺼내 같은지 비교
            if s in skill:
                # 만약 다르다면 선행스킬을 잘 안 따르는 것
                if s != skill_list.pop(0):
                    break
        # 만약 정상적으로 for문이 종료되었다면
        # 선행스킬을 잘 따르는 것
        else:
            answer += 1

    return answer
