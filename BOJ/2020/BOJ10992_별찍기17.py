N = int(input())
for n in range(N):
    if n == 0:
        print(" "*(N-1)+"*")
        continue
    if n == N-1:
        print("*"*(2*n+1))
        continue
    print(" "*(N-n-1)+"*"+" "*(2*n-1)+"*")