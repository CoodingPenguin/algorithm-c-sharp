def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        paper = queue.pop(0)
        if any(paper[1] < q[1] for q in queue):
            queue.append(paper)
        else:
            answer += 1
            if paper[0] == location:
                return answer
