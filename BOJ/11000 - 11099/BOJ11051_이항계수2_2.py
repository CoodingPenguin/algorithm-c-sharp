def factorial(n):
  if n in (0, 1):
    return 1
  count = 1
  while n > 1:
    count *= n
    n-=1
  return count

n, k = map(int, input().split())
result = factorial(n)//factorial(k)//factorial(n-k)

print(result%10007)