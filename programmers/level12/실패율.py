def solution(N, stages):
    stages.sort()
    fails = []
    for stage in range(1, N+1):
        try:
            fail = stages.count(stage) / len([x for x in stages if x >= stage])
        except:
            fail = 0
        fails.append(fail)
    result = sorted(range(1, N+1), key=lambda x: fails[x-1], reverse=True)
    return result
