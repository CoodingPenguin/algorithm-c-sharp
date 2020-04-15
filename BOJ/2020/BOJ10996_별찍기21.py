def result(n):
    if n == 1:
        print("*")
        return
    for i in range(2*n):
        for j in range(n):
            if (i+j) % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()


n = int(input())
result(n)
