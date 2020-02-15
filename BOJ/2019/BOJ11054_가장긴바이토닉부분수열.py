def fill_table(lst):
    for i in range(1, cnt + 1):
        lst[i] = 1
        for j in range(0, i, 1):
            if num[i] > num[j] and lst[i] < lst[j] + 1:
                lst[i] = lst[j] + 1

    return max(lst)


cnt = int(input())
num = [0]
parsing = input().split()
for i in range(cnt):
    num.append(int(parsing[i]))

dp_table = [0] * (cnt + 1)
dp_table_reverse = [0] * (cnt + 1)

# 정방향
fill_table(dp_table)

del num[0]
num.reverse()
num.insert(0, 0)

# 역방향
fill_table(dp_table_reverse)

dp_table_reverse.reverse()
dp_table_reverse.insert(0, 0)
del dp_table_reverse[-1]

for i in range(cnt+1):
    dp_table[i] = dp_table[i] + dp_table_reverse[i] - 1

print(max(dp_table))
