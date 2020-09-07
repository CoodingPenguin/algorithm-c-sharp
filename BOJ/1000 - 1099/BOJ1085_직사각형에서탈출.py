def shortest_path(x, y, w, h):
    return min(x, y, w-x, h-y)


x, y, w, h = map(int, input().split())
print(shortest_path(x, y, w, h))
