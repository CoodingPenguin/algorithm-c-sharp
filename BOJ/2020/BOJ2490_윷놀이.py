def result(yut):
    zeroCount = yut.count(0)
    if zeroCount == 0:
        return "E"
    elif zeroCount == 1:
        return "A"
    elif zeroCount == 2:
        return "B"
    elif zeroCount == 3:
        return "C"
    else:
        return "D"


for _ in range(3):
    yut = list(map(int, input().split()))
    print(result(yut))
