def result(s):
    rt = 2

    while s >= 0:
        if s - rt >= 0:
            s -= rt
            rt += 1
        else:
            break

    rt -= 1
    return rt


S = int(input())
print(result(S))
