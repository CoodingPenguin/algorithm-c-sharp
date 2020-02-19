N = int(input())

for i in range(1, N):
    print("*"*i+" "*(N-i)*2+"*"*i)
print("*"*(2*N))
for i in range(N-1, 0, -1):
    print("*"*i+" "*(N-i)*2+"*"*i)
