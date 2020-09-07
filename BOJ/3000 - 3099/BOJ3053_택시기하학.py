import math


def circle_area(r):
    print("{:.6f}".format(math.pi*(r**2)))
    print("{:.6f}".format(2*(r**2)))


circle_area(int(input()))
