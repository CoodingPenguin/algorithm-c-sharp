import sys

nums = [0]*10001
for i in range(int(sys.stdin.readline())):
  nums[int(sys.stdin.readline())] += 1
for num, count in enumerate(nums):
  if count:
    for _ in range(count):
      print(num)