def result(dn):
    bn = list(reversed((bin(dn)[2:])))

    for idx, b in enumerate(bn):
        if b == str(1):
            print(idx, end=" ")


for _ in range(int(input())):
    result(int(input()))
