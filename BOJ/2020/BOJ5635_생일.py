def one_2_two(digit):
    if len(digit) == 1:
        return "0" + digit
    else:
        return digit


N = int(input())
stds = {}

for n in range(N):
    std = list(input().split())
    stds[std[0]] = int(str(std[3])+str(one_2_two(std[2])) +
                       str(one_2_two(std[1])))

print(max(stds.keys(), key=stds.get))
print(min(stds.keys(), key=stds.get))
