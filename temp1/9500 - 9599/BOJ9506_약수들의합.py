def cal_factors(n):
    factors = []

    for i in range(1, n//2+1):
        if n % i == 0:
            factors.append(i)

    return factors


def result(n):
    myFactors = cal_factors(n)
    if n == sum(myFactors):
        rt = f"{n} = "
        for f in myFactors:
            rt += f"{f} + "
        return rt[:-2]
    else:
        return f"{n} is NOT perfect."


while True:
    N = int(input())
    if N == -1:
        break

    print(result(N))
