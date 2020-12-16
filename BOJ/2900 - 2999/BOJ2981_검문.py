import sys
import math


input = sys.stdin.readline

def solution(nums):
  # 두 수 차이의 최대공약수 계산
  diff = [x-y for x,y in zip(nums, nums[1:])]
  gcd = diff[0]
  for i in range(1, len(diff)):
    gcd = math.gcd(gcd, diff[i])
  
  # 최대공약수의 약수 계산
  result = list()
  for i in range(2, int(math.sqrt(gcd)+1)):
    if not gcd%i:
      result.extend([i, gcd//i])
  result.append(gcd)
  result = sorted(set(result))

  print(' '.join(map(str, result)))


if __name__ == "__main__":
  n = int(input())
  nums = list()
  for _ in range(n):
    nums.append(int(input()))
  solution(sorted(nums, reverse=True))