for _ in range(int(input())):
    i = list(map(int, input().split()))
    candy, children = i[0], i[1]
    print(
        f"You get {candy//children} piece(s) and your dad gets {candy%children} piece(s).")
