for _ in range(int(input())):
    ns = list(filter(lambda x: x % 2 == 0, map(int, input().split())))
    print(sum(ns), min(ns))
