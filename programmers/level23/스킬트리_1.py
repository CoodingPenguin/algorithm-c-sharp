import re


def solution(skill, skill_trees):
    answer = 0
    p = re.compile(f'[{skill}]')
    s_group = [skill[:i] for i in range(1, len(skill)+1)]
    for tree in skill_trees:
        result = ''.join(p.findall(tree))
        if result in s_group or len(result)==0:
            answer += 1
    return answer