l, r = int(input()), int(input()) / 100
count = 1
result = 0

while True:
    l = int(l*r)
    if l <= 5:
        break
    result += (2**count)*l
    count += 1

print(result)
