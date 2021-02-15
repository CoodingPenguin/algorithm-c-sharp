def result(xi):
    return 2*(xi[-1] - xi[0])


for _ in range(int(input())):
    input()
    xi = list(sorted(map(int, input().split())))
    print(result(xi))
