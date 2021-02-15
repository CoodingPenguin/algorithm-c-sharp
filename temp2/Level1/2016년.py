days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(a, b):
    total_days = sum(months[:a]) + b - 1
    return days[total_days%7]