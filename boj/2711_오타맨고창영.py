def result(idx, st):
    return st[:idx]+st[idx+1:]


for _ in range(int(input())):
    i = list(input().split())
    idx, miss = int(i[0])-1, i[1]

    print(result(idx, miss))
