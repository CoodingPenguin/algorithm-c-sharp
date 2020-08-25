import sys
from collections import Counter

def _average(nums):
  return round(sum(nums)/len(nums))


def _median(nums):
  sortedNums = sorted(nums)
  return sortedNums[len(nums)//2]


def _mode(nums):
  if len(nums) == 1:
    return nums[-1]
  counts = Counter(sorted(nums))
  mode = counts.most_common(2)
  if mode[0][1] == mode[1][1]:
    return mode[1][0]
  return mode[0][0]



def _range(nums):
  return max(nums) - min(nums)


nums = []
for _ in range(int(sys.stdin.readline())):
  nums.append(int(sys.stdin.readline()))

print(_average(nums))
print(_median(nums))
print(_mode(nums))
print(_range(nums))