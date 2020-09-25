def solution(progresses, speeds):
    rest_days = [(100-p)//s if (100-p) % s == 0 else (100-p) //
                 s+1 for p, s in zip(progresses, speeds)]
    stack = [rest_days[0]]
    result = []

    for day in rest_days[1:]:
        if day <= stack[0]:
            stack.append(day)
        else:
            count = 0
            while stack:
                stack.pop()
                count += 1
            result.append(count)
            stack.append(day)

    if stack:
        result.append(len(stack))

    return result
