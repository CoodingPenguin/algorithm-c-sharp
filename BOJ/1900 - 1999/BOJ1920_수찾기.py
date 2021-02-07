import sys

input = sys.stdin.readline

def binary_search(arr, start, end, target):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return True
    elif arr[mid] < target:
      start = mid+1
    else:
      end = mid-1
  return False


n = int(input())
n_list = sorted(map(int, input().split()))
m = int(input())
m_list = map(int, input().split())

for m_item in m_list:
  result = binary_search(n_list, 0, n-1, m_item)
  if result:
    print(1)
  else:
    print(0)
