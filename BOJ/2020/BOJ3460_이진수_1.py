def find_all(lst):
    idx = []
    for i, l in enumerate(lst):
        if l == 1:
            idx.append(i)
    return idx

def dec_2_bin(dn):
    binary = []
    while dn != 0:
        binary.append((dn % 2))
        dn //= 2
    return binary


def result(n):
    return find_all(dec_2_bin(n))


for _ in range(int(input())):
    for __ in result(int(input())):
        print(__, end=' ')
