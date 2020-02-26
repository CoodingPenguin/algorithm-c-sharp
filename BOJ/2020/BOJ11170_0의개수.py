for _  in range(int(input())):
    n, m = list(map(int, input().split()))
    rt = 0
    for i in range(n, m+1):
        rt += str(i).count('0')
    print(rt)