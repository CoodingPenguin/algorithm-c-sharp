import bisect

def count_by_range(arr, left, right):
  left_idx = bisect.bisect_left(arr, left)
  right_idx = bisect.bisect_right(arr, right)
  return right_idx - left_idx

n, x = map(int, input().split())
arr = list(map(int, input().split()))
result = count_by_range(arr, x, x)

if not result:
  print(-1)
else:
  print(result)