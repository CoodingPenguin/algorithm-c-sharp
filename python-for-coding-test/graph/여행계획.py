import sys
INF = int(1e9)
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i
for a in range(1, n+1):
  edges = list(map(int, input().split()))
  for b, flag in enumerate(edges):
    if flag:
      union_parent(parent, a, b+1)
plan = list(set(map(int, input().split())))
plan_parent = set([parent[node] for node in plan])
if len(plan_parent) == 1:
  print('YES')
else:
  print('NO')

