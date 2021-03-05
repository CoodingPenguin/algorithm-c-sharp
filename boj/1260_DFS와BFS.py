import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


# 입력
N, M, V = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for key in graph:
    graph[key].sort()

dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)

# 출력
dfs(graph, V, dfs_visited)
print()
bfs(graph, V, bfs_visited)
