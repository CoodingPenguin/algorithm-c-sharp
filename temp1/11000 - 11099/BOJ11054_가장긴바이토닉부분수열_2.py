def fill(n, nums, table, reversed=False):
      for i in range(1, n):
    sub = [table[j] for j in range(0, i) if nums[j] < nums[i] ]
    if sub:
      table[i] = max(sub) + 1
    else:
      table[i] = 0
  if reversed:
    return table[::-1]
  return table

def result(n, nums):
  down_table, up_table = [0]*n, [0]*n

  down_table = fill(n, nums, down_table)
  up_table = fill(n, nums[::-1], up_table, reversed=True)

  sum_lr = [x+y for x, y in zip(down_table, up_table)]
  return max(sum_lr) + 1

n = int(input())
nums = list(map(int, input().split()))
print(result(n, nums))