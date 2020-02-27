def bfs(graph, n):
    visit = [False]*n
    queue = list()
    queue.append(0)

    while queue:
        node = queue.pop(0)
        if not visit[node]:
            visit[node] = True
            queue.extend(graph[node])
    
    return visit


N, P = int(input()), int(input())
graph = [[] for _ in range(N)]

for _ in range(P):
    x, y = list(map(lambda x:int(x)-1, input().split()))
    graph[x].append(y)
    graph[y].append(x)

print(bfs(graph, N).count(True)-1)