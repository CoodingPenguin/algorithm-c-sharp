def is_primary(num):
    if num == 2 or num == 3:
        return True
    for i in range(2, num//2):
        if num % i == 0:
            return False

    return True


def genrate_primary(limit):
    primeMask = [False] * (limit+1)
    primeNumber = []

    for i in range(1, limit+1):
        if i == 1:
            continue
        if primeMask[i] == False:
            primeNumber.append(i)
            count = 2
            while i*count < limit+1:
                primeMask[i*count] = True
                count += 1

    return primeNumber


num = int(input())
result = []

if is_primary(num):
    result.append(num)
else:
    PRIMARY = genrate_primary(num//2)
    for p in PRIMARY:
        if num == 0:
            break
        while num % p == 0:
            result.append(p)
            num //= p

for rt in result:
    print(rt)
