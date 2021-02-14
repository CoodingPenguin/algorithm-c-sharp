import sys

input = sys.stdin.readline


def result(rooms, students, num_super, num_vice):
    count = rooms
    for n in students:
        rest = n - num_super
        if rest > 0:
            if rest % num_vice == 0:
                count += rest // num_vice
            else:
                count += rest // num_vice + 1
    return count


rooms = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

print(result(rooms, students, b, c))
