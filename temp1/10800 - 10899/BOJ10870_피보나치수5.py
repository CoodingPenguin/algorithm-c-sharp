def fibb(n):
    arr = [0]*21
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n]


print(fibb(int(input())))
