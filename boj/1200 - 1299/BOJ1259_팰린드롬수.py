import sys

input = sys.stdin.readline

while True:
    num = input().rstrip()
    if not int(num):
        break
    l = len(num)
    is_palindrome = all([num[i] == num[l - i - 1] for i in range(l // 2)])
    print("yes" if is_palindrome else "no")

