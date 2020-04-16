def add_zero(num):
    return "0"+str(num) if num < 10 else str(num)


def result(h, w, n):
    floor = n % h
    room = n//h+1
    if floor != 0:
        return str(floor)+add_zero(room)
    return str(h)+add_zero(room-1)


for _ in range(int(input())):
    h, w, n = map(int, input().split())
    print(result(h, w, n))
