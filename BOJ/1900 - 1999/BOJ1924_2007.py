def month_2_day(month):
    mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(mdays[:month-1])


days = {0:"MON", 1:"TUE", 2:"WED", 3:"THU", 4:"FRI", 5:"SAT", 6:"SUN"}

month, day = list(map(int, input().split()))
print(days[(month_2_day(month)+day-1)%7])