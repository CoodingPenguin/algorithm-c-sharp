serial = list(map(int, input().split()))
print(sum(map(lambda x: x**2, serial)) % 10)
